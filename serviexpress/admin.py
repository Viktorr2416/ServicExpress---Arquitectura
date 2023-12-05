from django.contrib import admin
from .models import Cliente, ReservaHora, Proveedor, Factura, Empleado, Servicio, Producto, OrdenPedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(ReservaHora)
admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Servicio)
admin.site.register(Factura)
admin.site.register(OrdenPedido)
admin.site.register(Producto)

