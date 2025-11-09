from django.shortcuts import render
from .models import Producto, Evento, Sucursal, Vehiculo, Comentario

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def autos(request):
    autos = Vehiculo.objects.all()
    return render(request, 'autos.html', {'autos':autos})

def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales.html', {'sucursales': sucursales})

def comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comentarios.html', {'comentarios': comentarios})