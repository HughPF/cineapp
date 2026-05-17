from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'sinopsis', 'anio', 'duracion', 'genero', 'cartel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'campo', 'placeholder': 'Título de la película'}),
            'director': forms.TextInput(attrs={'class': 'campo', 'placeholder': 'Director/a'}),
            'sinopsis': forms.Textarea(attrs={'class': 'campo', 'rows': 4, 'placeholder': 'Resumen de la película...'}),
            'anio': forms.NumberInput(attrs={'class': 'campo', 'min': 1888, 'max': 2100}),
            'duracion': forms.NumberInput(attrs={'class': 'campo', 'min': 1}),
            'genero': forms.Select(attrs={'class': 'campo'}),
            'cartel': forms.ClearableFileInput(attrs={'class': 'campo'}),
        }


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'campo', 'placeholder': 'tu@email.com'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'campo', 'placeholder': 'Nombre de usuario'})
        self.fields['password1'].widget.attrs.update({'class': 'campo'})
        self.fields['password2'].widget.attrs.update({'class': 'campo'})
