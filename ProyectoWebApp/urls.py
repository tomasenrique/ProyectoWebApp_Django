"""
Este archivo se crea para poder ordenar las vistas de una aplicacion dentro de un proyecto, de esta forma cuando se
tenga mas aplicaciones dentro de un proyecto, se creara dentro de cada aplicacion un archivo 'urls' que se enlazara
con el 'urls' principal del proyecto y aqui solo se tendra que poder las url como se muestran abajo y en el principal
del proyecto pondria asi:
                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path("ProyectoWebApp/", include("ProyectoWebApp.urls")),
                ]
Donde:
'ProyectoWebApp/'                ==>> Viene a ser el nombre de la aplicacion pero podemos usar el que queramos ya que
                                      este viene a ser el enlace con el cual se ubicara en la pagina web.
'include("ProyectoWebApp.urls")' ==>> Este seria una funcion que agregara todas las url de la aplicacion al proyecto
                                      principal poniendo su nombre y usando la nomenclatura del punto para ubicar las
                                      url de la aplicacion.
"""
from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('home/', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
]
