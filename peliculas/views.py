from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
)

from .models import Pelicula, Genero
from .forms import PeliculaForm, RegistroForm


class StaffOrAuthorMixin(UserPassesTestMixin):
    """Permite acceso al autor del objeto o a usuarios staff/superuser."""

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user.is_staff or user.is_superuser or obj.autor == user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                'No tienes permiso para realizar esta acción. Solo el autor o un administrador pueden modificar este contenido.'
            )
            return redirect('pelicula_list')
        return super().handle_no_permission()


class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'peliculas/pelicula_list.html'
    context_object_name = 'peliculas'
    paginate_by = 8

    def get_queryset(self):
        queryset = Pelicula.objects.select_related('genero', 'autor').all()
        query = self.request.GET.get('q', '').strip()
        genero_id = self.request.GET.get('genero', '').strip()

        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(director__icontains=query) |
                Q(sinopsis__icontains=query)
            )
        if genero_id.isdigit():
            queryset = queryset.filter(genero_id=int(genero_id))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        context['query'] = self.request.GET.get('q', '')
        context['genero_seleccionado'] = self.request.GET.get('genero', '')
        return context


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'peliculas/pelicula_detail.html'
    context_object_name = 'pelicula'


class PeliculaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/pelicula_form.html'
    success_message = 'La película "%(titulo)s" se ha creado correctamente.'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Añadir nueva película'
        context['boton'] = 'Crear'
        return context


class PeliculaUpdateView(LoginRequiredMixin, StaffOrAuthorMixin, SuccessMessageMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/pelicula_form.html'
    success_message = 'La película "%(titulo)s" se ha actualizado correctamente.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = f'Editar: {self.object.titulo}'
        context['boton'] = 'Guardar cambios'
        return context


class PeliculaDeleteView(LoginRequiredMixin, StaffOrAuthorMixin, DeleteView):
    model = Pelicula
    template_name = 'peliculas/pelicula_confirm_delete.html'
    success_url = reverse_lazy('pelicula_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            f'La película "{self.object.titulo}" se ha eliminado correctamente.'
        )
        return super().form_valid(form)


class RegistroView(SuccessMessageMixin, FormView):
    template_name = 'registration/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('pelicula_list')
    success_message = '¡Bienvenido/a, %(username)s! Tu cuenta se ha creado correctamente.'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
