from django.shortcuts import render

# para importar los datos de las clases que hay en el archivo 'models' de la carpeta de la app de 'Servicios'
from Servicios.models import Servicio


def servicios(request):
    """ Desde este archivo 'views' hay que importar todos los Servicios que se carguen en el panel de administracion y
    luego decirle que los muestre en el template asignado a cada vista, en este caso 'Servicios.html'      """

    servicios = Servicio.objects.all()  # importara todos los objetos que halla en la clase 'Servicios'

    diccionario_servicio = {"Servicios": servicios}  # para almacenar los datos a mostrar
    # devuelve un renderizado del template servicio
    return render(request, "../templates/servicios/servicios.html", diccionario_servicio)

