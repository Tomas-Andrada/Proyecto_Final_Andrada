from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    path('usuario/<int:id_user>/', views.ver_perfil, name='perfil'),
     path('agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)