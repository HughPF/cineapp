from django.views.generic import ListView, DetailView, CreateView

from .models import Pelicula
from .forms import PeliculaForm


class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'peliculas/pelicula_list.html'
    context_object_name = 'peliculas'
    paginate_by = 8


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'peliculas/pelicula_detail.html'
    context_object_name = 'pelicula'


class PeliculaCreateView(CreateView):
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
