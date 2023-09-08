from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegistroUsuarioForm

def inicio_sesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "BlogAndrada/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request,"BlogAndrada/inicio_sesion.html", {"form":form, "mensaje":"Datos invalidos"})
        else:
            return render(request,"BlogAndrada/inicio_sesion.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=AuthenticationForm()
        return render(request,"BlogAndrada/inicio_sesion.html", {"form":form})

def registro(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "BlogAndrada/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente, inicie sesion"})
        else:
            return render(request,"BlogAndrada/registro.html", {"form":form, "mensaje":"Datos invalidos"})

    else:
        form=RegistroUsuarioForm()
        return render(request,"BlogAndrada/registro.html", {"form":form})