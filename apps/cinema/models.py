from django.db import models
from django.utils import timezone

# Create your models here.

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    Direccion = models.CharField(max_length=220, blank=False, null=False)
    TipoServicio = models.CharField(max_length=100, blank=False, null=False)
    PrecioBoleto = models.TextField(blank=False, null=False)
    Distrito = models.TextField(max_length=100, blank=False, null=False)
    ImagenL = models.ImageField(upload_to='pictures/local',blank=True, null=False)

    class Meta:
        verbose_name= 'Local'
        verbose_name_plural= 'Locales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.TextField(max_length=100, blank=False, null=False)
    imagenA = models.ImageField(upload_to='pictures/actor',blank=True, null=False)

    class Meta:
        verbose_name= 'Actor'
        verbose_name_plural= 'Actores'
        ordering = ['nombres']

    def __str__(self):
        return self.nombres

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=100, blank=False, null=False)
    trailer = models.TextField(max_length=100, blank=False, null=False)
    categoria = models.TextField(max_length=100, blank=False, null=False)
    genero = models.TextField(max_length=100, blank=False, null=False)
    imagenP = models.ImageField(upload_to='pictures/pelicula',blank=True, null=False)
    sinopsis =  models.TextField(max_length=100, blank=False, null=False)
    director = models.TextField(max_length=100, blank=False, null=False)
    idioma = models.TextField(max_length=100, blank=False, null=False)  
    actor = models.ManyToManyField(Actor)

    class Meta:
        verbose_name= 'Pelicula'
        verbose_name_plural= 'Peliculas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class Funcion(models.Model):
    id = models.AutoField(primary_key=True)
    local = models.ForeignKey('cinema.Local', on_delete=models.CASCADE)
    pelicula = models.ForeignKey('cinema.pelicula', on_delete=models.CASCADE)
    Sala = models.TextField(max_length=50, blank=False, null=False)
    fecha = models\
                   .DateTimeField(
                    default = timezone.now
                   )


    def publish(self):
        self.fecha = timezone.now()
        self.save()

    class Meta:
        verbose_name= 'Funcion'
        verbose_name_plural= 'Funciones'
        ordering = ['local']

    def __str__(self):
        return self.local

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    funcion = models.ForeignKey('cinema.funcion', on_delete=models.CASCADE)
    cantidad = models.TextField(max_length=50, blank=False, null=False)
    total = models.TextField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name= 'Reserva'
        verbose_name_plural= 'Reservas'
        ordering = ['funcion']

    def __str__(self):
        return self.funcion