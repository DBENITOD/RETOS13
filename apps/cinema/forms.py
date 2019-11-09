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

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula 
        fields = ['titulo','trailer','categoria','genero','imagenP','sinopsis','director','idioma']
        labels = {
            'titulo': 'Titulo de la Pelicula',
            'trailer': 'Trailer de la Pelicula',
            'categoria': 'Categoria de la Pelicula',
            'genero': 'Genero de la Pelicula',
            'imagenP': 'Avatar de la Pelicula',
            'sinopsis': 'Sinopsis de la Pelicula',
            'director': 'Director de la Pelicula',
            'idioma': 'Idioma de la Pelcula'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el Titulo de la Pelicula ',
                    'id': 'titulo'
                }
            ),
             'trailer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el Trailer de la Pelicula ',
                    'id': 'trailer'
                }
            ),
             'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la Categoria de la Pelicula ',
                    'id': 'categoria'
                }
            ),
             'genero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el Genero de la Pelicula ',
                    'id': 'genero'
                }
            ),
            'imagenP': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagenP'
                }
            ),
             'sinopsis': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la Sinopsis de la Pelicula ',
                    'id': 'sinopsis'
                }
            ),
             'director': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el Director de la Pelicula ',
                    'id': 'director'
                }
            ),
             'idioma': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el Idioma de la Pelicula ',
                    'id': 'idioma'
                }
            )
        }