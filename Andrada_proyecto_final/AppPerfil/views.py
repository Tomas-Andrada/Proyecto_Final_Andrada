from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserEditForm, AvatarForm
from .models import Avatar,Perfil
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
@login_required
def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    
    if len(avatares)!=0:
        
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"

@login_required
def editarPerfil(request):
    usuario = request.user
    perfil, created = Perfil.objects.get_or_create(usuario=usuario)
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.username = info["username"]
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            perfil.descripcion = info["descripcion"]  #
            usuario.save()
            perfil.save()
            return render(request, "BlogAndrada/inicio.html", {"mensaje": f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "BlogAndrada/editarPerfil.html", {"form": form, "mensaje": "Datos inválidos"})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "BlogAndrada/editarPerfil.html", {"form": form, "nombreusuario": usuario.username})
def ver_perfil(request, id_user):
     usuario = get_object_or_404(User, id=id_user)
     imagen=obtenerAvatar(request)
     return render(request, 'BlogAndrada/perfil.html', {"usuario": usuario,"imagen":imagen})


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "BlogAndrada/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "BlogAndrada/agregaravatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "BlogAndrada/agregaravatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})