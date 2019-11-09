from django.contrib import admin
from .models import Actor,Pelicula,Funcion,Reserva,Local

# Register your models here.
admin.site.register(Actor)
admin.site.register(Pelicula)
admin.site.register(Funcion)
admin.site.register(Reserva)
admin.site.register(Local)
