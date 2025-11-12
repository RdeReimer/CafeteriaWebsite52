from django.db import models
from django.utils import timezone
import random

# Create your models here.

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    TIPO_OPCIONES = [
        ('auto', 'Auto'),
        ('moto', 'Moto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_OPCIONES)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    nombre_conductor = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} - {self.nombre_conductor}"


class Producto(models.Model):
    CATEGORIAS = [
        ('normal', 'Normal'),
        ('navidad', 'Navidad'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='normal')

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"


class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    direccion_entrega = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.producto}"
    
    def asignar_reparto(self):
        vehiculos_disponibles = Vehiculo.objects.filter(disponible=True)
        if vehiculos_disponibles.exists():
            elegido = random.choice(vehiculos_disponibles)
            self.vehiculo = elegido
            self.save()
            return elegido
        return None


class Comentario(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre_cliente}"

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
    
class reseña(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=[(i, f"{i} estrellas") for i in range(1,6)])
    comentario = models.TextField(max_length=500)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.calificacion}⭐"
