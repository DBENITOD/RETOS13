from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListarActores, CrearActor, EditarActor, EliminarActor
from .views import ListarLocales, CrearLocal, EditarLocal, EliminarLocal

urlpatterns = [
    #actores
    path('listar_actores/', login_required(ListarActores.as_view()), name='listar_actores'),
    path('crear_actor/', CrearActor.as_view(), name='crear_actor'),
    path('editar_actor/<int:pk>', EditarActor.as_view(), name='editar_actor'),
    path('eliminar_actor/<int:pk>', EliminarActor.as_view(), name='eliminar_actor'),
    
    #locales
    path('listar_locales/', login_required(ListarLocales.as_view()), name='listar_locales'),
    path('crear_local/', CrearLocal.as_view(), name='crear_local'),
    path('editar_local/<int:pk>', EditarLocal.as_view(), name='editar_local'),
    path('eliminar_local/<int:pk>', EliminarLocal.as_view(), name='eliminar_local'),
]