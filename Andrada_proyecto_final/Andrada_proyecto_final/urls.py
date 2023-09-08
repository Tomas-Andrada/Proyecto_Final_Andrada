from django.contrib import admin
from django.urls import path,include
from BlogAndrada.views import inicio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path("blog/", include("BlogAndrada.urls")),
    path("login/", include("AppLogin.urls")),
    path("perfil/", include("AppPerfil.urls")),
    path("chat/", include("Appchat.urls")),
]
