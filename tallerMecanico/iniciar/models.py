from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class administrador(AbstractUser):
    es_administrador = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='cliente')  
    user_permissions = models.ManyToManyField(Permission, related_name='cliente_permiso')

class usuario(models.Model):
    usuario = models.OneToOneField(administrador, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=255, blank=True, null=True)
    correo_cliente = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username

