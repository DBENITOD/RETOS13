from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import ActorForm, LocalForm
from .models import Actor, Pelicula, Funcion, Reserva, Local
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Home(TemplateView):
    template_name = 'cinema/actor/index.html'

    def get_context_data(self, *args, **kwargs):
        actor = Actor.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['actores'] = actor
        return context

#ACTORES
class ListarActores(ListView):
    model = Actor
    template_name = 'cinema/actor/listar_actor.html'
    queryset = Actor.objects.all()
    context_object_name = 'actores'

class CrearActor(CreateView):
    model = Actor
    form_class = ActorForm
    template_name = 'cinema/actor/crear_actor.html'
    success_url = reverse_lazy('cinema:listar_actores')

class EditarActor(UpdateView):
    model = Actor
    form_class = ActorForm
    template_name = 'cinema/actor/editar_actor.html'
    success_url = reverse_lazy('cinema:listar_actores')

class EliminarActor(DeleteView):
    model = Actor
    form_class = ActorForm
    template_name = 'cinema/actor/eliminar_actor.html'
    success_url = reverse_lazy('cinema:listar_actores')

    def get_context_data(self, *args, **kwargs):
        actor = Actor.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarActor, self).get_context_data(*args, **kwargs)
        context['actor'] = actor
        return context

#LOCALES
class ListarLocales(ListView):
    model = Local
    template_name = 'cinema/local/listar_locales.html'
    queryset = Local.objects.all()
    context_object_name = 'locales'

class CrearLocal(CreateView):
    model = Local
    form_class = LocalForm
    template_name = 'cinema/local/crear_local.html'
    success_url = reverse_lazy('cinema:listar_locales')

class EditarLocal(UpdateView):
    model = Local
    form_class = LocalForm
    template_name = 'cinema/local/editar_local.html'
    success_url = reverse_lazy('cinema:listar_locales')

class EliminarLocal(DeleteView):
    model = Local
    form_class = LocalForm
    template_name = 'cinema/local/eliminar_local.html'
    success_url = reverse_lazy('cinema:listar_locales')

    def get_context_data(self, *args, **kwargs):
        local = Local.objects.get(id=self.kwargs.get('pk'))
        context = super(EliminarLocal, self).get_context_data(*args, **kwargs)
        context['local'] = local
        return context        