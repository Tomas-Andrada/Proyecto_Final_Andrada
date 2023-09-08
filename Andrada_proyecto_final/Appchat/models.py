from django.db import models
from django.contrib.auth.models import User

class MensajeChat(models.Model):
    remitente=models.ForeignKey(User, on_delete=models.CASCADE)
    contenido=models.TextField()
    fecha_envio=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De: {self.remitente.username} - Contenido: {self.contenido}"