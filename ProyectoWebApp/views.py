from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")


def servicios(request):
    return render(request, "ProyectoWebApp/servicios.html")


def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")


def block(request):
    return render(request, "ProyectoWebApp/block.html")


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")
