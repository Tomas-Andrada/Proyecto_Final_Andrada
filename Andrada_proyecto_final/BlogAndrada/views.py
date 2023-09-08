
from django.shortcuts import render,get_object_or_404
from .models import Blog
from .forms import BlogForm   
from django.db import models
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "BlogAndrada/inicio.html")
def acerca_de_mi(request):
    return render(request, 'BlogAndrada/acerca_de_mi.html')
@login_required
def listar_blogs(request):
    blogs=Blog.objects.all()
    return render(request, "BlogAndrada/listar_blogs.html", {"blogs": blogs})
@login_required
def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            
            nuevo_blog = Blog(
                titulo=form.cleaned_data['titulo'],
                subtitulo=form.cleaned_data['subtitulo'],
                cuerpo=form.cleaned_data['cuerpo'],
                imagen=form.cleaned_data['imagen'],
                autor=request.user 
            )
            nuevo_blog.save()
            
            return render(request,'BlogAndrada/inicio.html',{"mensaje":"Blog creado",'form': form})  
    else:
        form = BlogForm()
        return render(request,'BlogAndrada/crear_blog.html',{"mensaje":"Datos invalidos",'form': form})  
    return render(request, 'BlogAndrada/crear_blog.html',{'form': form})
@login_required
def detalle_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'BlogAndrada/detalle_blog.html', {'blog': blog})
@login_required
def editarBlog(request, id):
    blog = Blog.objects.get(id=id)
    if blog.autor == request.user:
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                info = form.cleaned_data
                blog.titulo = info["titulo"]
                blog.subtitulo = info["subtitulo"]
                blog.cuerpo = info["cuerpo"]
                blog.imagen = info["imagen"]
                blog.save()
                form = BlogForm()
                blogs=Blog.objects.all()
                return render(request, 'BlogAndrada/inicio.html', {'form': form, 'blogs': blogs, "mensaje": "Blog editado con exito"})
        else:
            form = BlogForm(initial={"titulo": blog.titulo, "subtitulo": blog.subtitulo, "cuerpo": blog.cuerpo, "imagen": blog.imagen})
        return render(request, 'BlogAndrada/editar_blog.html', {'blog': blog, "form": form})

@login_required
def eliminar_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    # Verifica si el usuario actual es el autor del blog
    if blog.autor == request.user:
        if request.method == "POST":
            blog.delete()
            # Redirige o renderiza según tu preferencia
            blogs = Blog.objects.all()
            return render(request, "BlogAndrada/inicio.html", {"blogs": blogs, "mensaje": "Blog eliminado con éxito"})
        else:
            return render(request, "BlogAndrada/eliminar_blog.html", {"blog": blog})
