from django.db import models

# Create your models here.
class prueba(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)

# Datos de Cliente
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=8)

# Datos de Reserva Hora
class ReservaHora(models.Model):
    id = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente)
    horafecha= models.DateTimeField()
    servicio = models.CharField(max_length=50)

# Datos de Proveedor
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nom_empresa = models.CharField(max_length=50)
    contacto = models.CharField(max_length=30)
    rubro = models.CharField(max_length=80)
    
# Datos de Factura
class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente)
    fecha = models.DateTimeField()
    detalle = models.CharField(max_length=150)
    totalPagar = models.IntegerField()

# Datos de Empleado
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

# Datos de Servicio 
class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    Empleado = models.ForeignKey(Empleado)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

# Datos de Producto 
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nom_producto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    precio_uni = models.IntegerField()

# Datos Orden de Pedido
class OrdenPedido(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor)
    empleado = models.ForeignKey(Empleado)
    fecha_solicitud = models.DateTimeField()
    productos = models.ManyToManyField(Producto, through='DetalleOrdenPedido')

# Datos DetalleOrdenPedido
class DetalleOrdenPedido(models.Model):
    orden_pedido = models.ForeignKey(OrdenPedido)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    subtotal = models.IntegerField()

# Datos Recepcion de Producto
class RecepcionProducto(models.Model):
    id = models.AutoField(primary_key=True)
    orden_pedido = models.ForeignKey(OrdenPedido)
    producto = models.ForeignKey(Producto)
    fechaRecepcion = models.DateTimeField()
    