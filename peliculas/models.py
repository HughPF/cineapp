from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    director = models.CharField(max_length=150, verbose_name='Director/a')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    anio = models.PositiveIntegerField(verbose_name='Año de estreno')
    duracion = models.PositiveIntegerField(
        verbose_name='Duración (minutos)', default=90
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
