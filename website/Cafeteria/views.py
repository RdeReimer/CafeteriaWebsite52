from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Evento, Sucursal, Vehiculo, Comentario, reseña
from .forms import ReseñaForm

# Create your views here.

def inicio(request):
    productos = Producto.objects.filter(categoria='normal')[:4]
    return render(request, 'index.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.filter(categoria='normal')
    return render(request, 'productos.html', {'productos': productos})

def eventos(request):
    productos_navidad = Producto.objects.filter(categoria='navidad')
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos, 'productos_navidad': productos_navidad})
=======
    return render(request, 'cafeteria.html')

# def productos(request):
#     productos = Producto.objects.all()
#     return render(request, 'productos.html', {'productos': productos})

# def eventos(request):
#     eventos = Evento.objects.all()
#     return render(request, 'eventos.html', {'eventos': eventos})
>>>>>>> fb531950e6374e2834c01e4042a869e338bc3415

# def autos(request):
#     autos = Vehiculo.objects.all()
#     return render(request, 'autos.html', {'autos':autos})

def sucursales(request):
     sucursales = Sucursal.objects.all()
     return render(request, 'sucursales.html', {'sucursales': sucursales})

def comentarios(request):
    reseñas = reseña.objects.order_by('-fecha')[:3]
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentarios')
    else:
        form = ReseñaForm()
    return render(request, 'comentarios.html', {'reseñas': reseñas, 'form': form})

def finalizar_compra(request):
    messages.success(request, "Gracias por tu compra! Te gustaria dejar una reseña sobre tu experiencia?")
    return redirect('comentarios')
