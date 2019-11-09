from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import ActorForms
from .models import Actor, Pelicula, Funcion, Reserva, Local
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Home(TemplateView):
    pass