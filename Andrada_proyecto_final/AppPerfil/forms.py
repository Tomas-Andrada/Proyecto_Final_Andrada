from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
    username=forms.CharField(label="Usuario")
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), required=False)

    class Meta:
        model=User
        fields=["username","email", "password1", "password2", "first_name", "last_name","descripcion"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")