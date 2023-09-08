from django.contrib import admin
from django.urls import path
from AppLogin import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('registro/', views.registro, name='registro'), 
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/',LogoutView.as_view(next_page='inicio_sesion'),name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)