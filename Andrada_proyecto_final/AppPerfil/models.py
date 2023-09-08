from django.db import models
from django.contrib.auth.models import User
class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.usuario.username