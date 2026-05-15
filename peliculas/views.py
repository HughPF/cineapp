from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
)

from .models import Pelicula
from .forms import PeliculaForm, RegistroForm


class StaffOrAuthorMixin(UserPassesTestMixin):
    """Permite acceso al autor del objeto o a usuarios staff/superuser."""

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user.is_staff or user.is_superuser or obj.autor == user


class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'peliculas/pelicula_list.html'
    context_object_name = 'peliculas'
    paginate_by = 8


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'peliculas/pelicula_detail.html'
    context_object_name = 'pelicula'


class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/pelicula_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Añadir nueva película'
        context['boton'] = 'Crear'
        return context


class PeliculaUpdateView(LoginRequiredMixin, StaffOrAuthorMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/pelicula_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = f'Editar: {self.object.titulo}'
        context['boton'] = 'Guardar cambios'
        return context


class PeliculaDeleteView(LoginRequiredMixin, StaffOrAuthorMixin, DeleteView):
    model = Pelicula
    template_name = 'peliculas/pelicula_confirm_delete.html'
    success_url = reverse_lazy('pelicula_list')


class RegistroView(FormView):
    template_name = 'registration/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('pelicula_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
