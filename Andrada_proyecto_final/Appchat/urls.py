from django.urls import path
from . import views

urlpatterns = [
    path('listar_mensajes/', views.listar_mensajes, name='listar_mensajes'),
    path('crear_mensaje/', views.Crear_mensaje, name='crear_mensaje'),
    path('editar_mensaje/<int:id>/', views.editarmensaje, name='editar_mensaje'),
    path('eliminar_mensaje/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
]