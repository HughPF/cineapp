from django.views.generic import ListView, DetailView

from .models import Pelicula


class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'peliculas/pelicula_list.html'
    context_object_name = 'peliculas'
    paginate_by = 8


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'peliculas/pelicula_detail.html'
    context_object_name = 'pelicula'
