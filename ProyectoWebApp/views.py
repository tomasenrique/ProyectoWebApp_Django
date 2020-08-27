from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# para importar los datos de las clases que hay en el archivo 'models' de la carpeta de la app de 'servicios'
from servicios.models import Servicio


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")


def servicios(request):
    """ Desde este archivo 'views' hay que importar todos los servicios que se carguen en el panel de administracion y
    luego decirle que los muestre en el template asignado a cada vista, en este caso 'servicios.html'      """

    servicios = Servicio.objects.all()  # importara todos los objetos que halla en la clase 'Servicios'

    diccionario_servicio = {"servicios": servicios}  # para almacenar los datos a mostrar
    # devuelve un renderizado del template servicio
    return render(request, "ProyectoWebApp/servicios.html", diccionario_servicio)


def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")


def blog(request):
    return render(request, "ProyectoWebApp/blog.html")


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")
