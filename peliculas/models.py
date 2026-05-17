from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    descripcion = models.CharField(max_length=200, blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    director = models.CharField(max_length=150, verbose_name='Director/a')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    anio = models.PositiveIntegerField(verbose_name='Año de estreno')
    duracion = models.PositiveIntegerField(
        verbose_name='Duración (minutos)', default=90
    )
    cartel = models.ImageField(
        upload_to='carteles/', blank=True, null=True, verbose_name='Cartel'
    )
    genero = models.ForeignKey(
        Genero, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='peliculas', verbose_name='Género'
    )
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='peliculas', verbose_name='Autor/a'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación'
    )
    fecha_modificacion = models.DateTimeField(
        auto_now=True, verbose_name='Última modificación'
    )

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f'{self.titulo} ({self.anio})'

    def get_absolute_url(self):
        return reverse('pelicula_detail', kwargs={'pk': self.pk})
