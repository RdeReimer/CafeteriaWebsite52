from django.db import models

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
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre


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