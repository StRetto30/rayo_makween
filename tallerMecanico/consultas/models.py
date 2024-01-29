from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Mecanico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Atencion(models.Model):
    titulo = models.CharField(max_length=255)
    diagnostico = models.TextField()
    fecha = models.DateField()
    imagenes = models.ImageField(upload_to='atenciones/')
    aprobado = models.BooleanField(default=False)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)

