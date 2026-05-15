from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('pelicula/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
]
