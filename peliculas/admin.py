from django.contrib import admin
from .models import Pelicula, Genero


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'anio', 'genero', 'autor', 'fecha_creacion')
    list_filter = ('genero', 'anio', 'autor')
    search_fields = ('titulo', 'director', 'sinopsis')
    date_hierarchy = 'fecha_creacion'
