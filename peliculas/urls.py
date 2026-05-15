from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('pelicula/nueva/', views.PeliculaCreateView.as_view(), name='pelicula_create'),
    path('pelicula/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
    path('pelicula/<int:pk>/editar/', views.PeliculaUpdateView.as_view(), name='pelicula_update'),
    path('pelicula/<int:pk>/eliminar/', views.PeliculaDeleteView.as_view(), name='pelicula_delete'),
]
