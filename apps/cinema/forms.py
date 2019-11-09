from django import forms
from .models import Actor,Pelicula,Funcion,Reserva,Local


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombres','imagenA']
        labels = {
            'nombres': 'Nombres del autor',
            'imagenA': 'Avatar del autor'
        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa los datos del autor',
                    'id': 'nombres'
                }
            ),
            'imagenA': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagenA'
                }
            )
        }