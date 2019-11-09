from django import forms
from .models import Actor,Pelicula,Funcion,Reserva,Local


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombres','imagenA']
        labels = {
            'nombres': 'Nombres del actor',
            'imagenA': 'Avatar del actor'
        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa los datos del actor',
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

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre','Direccion','TipoServicio','PrecioBoleto','Distrito','ImagenL']
        labels = {
            'nombre': 'Nombres del local',
            'Direccion': 'Direccion del local',
            'TipoServicio': 'Tipo de servicio del local',
            'PrecioBoleto': 'Precio de Boleto',
            'Distrito': 'Distrito del local',
            'ImagenL': 'Avatar del local'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa los datos del Local',
                    'id': 'nombre'
                }
            ),
            'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la direccion del Local',
                    'id': 'Direccion'
                }
            ),
            'TipoServicio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa los servicios del local [D | P | M | S]',
                    'id': 'TipoServicio'
                }
            ),
            'PrecioBoleto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el precio del Boleto',
                    'id': 'PrecioBoleto'
                }
            ),
            'Distrito': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el distrito del Local',
                    'id': 'Distrito'
                }
            ),
            'ImagenL': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'ImagenL'
                }
            )
        }