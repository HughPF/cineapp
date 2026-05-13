from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeliculaListView.as_view(), name='pelicula_list'),
]
