from django.contrib import admin
from .models import Producto, Vehiculo, Sucursal, Pedido, Comentario, Evento

# Register your models here.

admin.site.register(Producto)
admin.site.register(Vehiculo)
admin.site.register(Sucursal)
admin.site.register(Pedido)
admin.site.register(Comentario)
admin.site.register(Evento)