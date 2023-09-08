from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('crear_blog/', views.crear_blog, name='crear_blog'),
    path('blog/detalle/<int:blog_id>/', views.detalle_blog, name='detalle_blog'),    
    path('blog/eliminar/<int:blog_id>/', views.eliminar_blog, name='eliminar_blog'),
    path('blog/detalle/<int:blog_id>/', views.detalle_blog, name='detalle_blog'),
    path('editar_blog/<int:id>/', views.editarBlog, name='editar_blog'),
    path('listar_blogs',views.listar_blogs,name='listar_blogs'),


    path('acerca_de_mi/',views.acerca_de_mi, name='acerca_de_mi'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)