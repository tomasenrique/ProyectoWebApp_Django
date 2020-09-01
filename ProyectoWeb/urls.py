"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings  # Para agregar la ubicacion de almacenamiento de las imagenes
from django.conf.urls.static import static  # Para agregar la url de la ubicacion del almacenamiento

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ProyectoWebApp/", include("ProyectoWebApp.urls")),  # Agrega las urls de una aplicacion
    path('Servicios/', include('Servicios.urls'))  # agrega una aplicacion llamada servicios con sus urls

]

# Concatena las variables para poder agregar la ubicacion y la url de la ubicacion de las imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
OJO ==>> esta es el archivo 'urls' principal del sistema

"""
