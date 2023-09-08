from django.shortcuts import render,get_object_or_404
from .forms import MensajeForm
from .models import MensajeChat
from django.contrib.auth.decorators import login_required
@login_required
def listar_mensajes(request):
    mensajes=MensajeChat.objects.all()
    return render(request, "BlogAndrada/chat_global.html", {"mensajes": mensajes})
from django.contrib.auth.decorators import login_required
from .models import MensajeChat
from .forms import MensajeForm  

@login_required
def Crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST, request.FILES)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            remitente = request.user  
            mensaje = MensajeChat(contenido=contenido, remitente=remitente)
            mensaje.save()
            return render(request, 'BlogAndrada/inicio.html', {"mensaje": "Mensaje creado", 'form': form})
    else:
        form = MensajeForm()
    return render(request, 'BlogAndrada/Crear_mensaje.html', {'form': form})

@login_required
def editarmensaje(request, id):
    mensaje = MensajeChat.objects.get(id=id)
    
    if mensaje.remitente == request.user:
        if request.method == "POST":
            form = MensajeForm(request.POST, request.FILES)
            if form.is_valid():
                info = form.cleaned_data
                mensaje.contenido = info["contenido"]
                mensaje.save()
                form = MensajeForm()  
                return render(request, 'BlogAndrada/inicio.html', {'form': form, 'mensaje': mensaje, "mensaje": "Mensaje editado"})
        else:
            form = MensajeForm(initial={"contenido": mensaje.contenido})  
        return render(request, 'BlogAndrada/editar_mensaje.html', {'mensaje': mensaje, "form": form})
    else:
        return render(request, "BlogAndrada/chat_golbal.html", {"mensaje": mensaje, "mensaje": "No tienes permitido editar este mensaje"})
    

@login_required
def eliminar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(MensajeChat, pk=mensaje_id)
    if mensaje.remitente == request.user:
        mensaje.delete()
        mensaje = MensajeChat.objects.all()
        return render(request, "BlogAndrada/chat_global.html", {"mensaje": mensaje, "mensaje": "Mensaje eliminado"})
    else:
        return render(request, "BlogAndrada/chat_global.html", {"mensaje": mensaje, "mensaje": "No tienes permitido borrar este mensaje"})
   
