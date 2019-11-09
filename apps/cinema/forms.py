from django import forms
from .models import Actor,Pelicula,Funcion,Reserva,Local


class ActorForms(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombres','imagenA']
        widgets = {
            'nombres': forms.TextInput
        }