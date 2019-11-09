from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListarActores, CrearActor, EditarActor, EliminarActor

urlpatterns = [
    path('listar_actores/', login_required(ListarActores.as_view()), name='listar_actores'),
    path('crear_actor/', CrearActor.as_view(), name='crear_actor'),
    path('editar_actor/<int:pk>', EditarActor.as_view(), name='editar_actor'),
    path('eliminar_actor/<int:pk>', EliminarActor.as_view(), name='eliminar_actor'),
]