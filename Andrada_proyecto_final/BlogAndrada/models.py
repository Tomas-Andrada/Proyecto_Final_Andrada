from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_imagenes')
    def __str__(self):
        return f"Titulo: {self.titulo} - De: {self.autor}"