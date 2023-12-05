from django.db import models
from django import forms

# Datos de Cliente
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=8)

# Datos de Reserva Hora
class ReservaHora(models.Model):
    id = models.AutoField(primary_key=True)
    hora= models.TimeField()
    fecha=models.DateField()
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
    fecha = models.DateField()
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
    nombre = models.CharField(max_length=20)
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
    fecha_solicitud = models.DateField()
    nom_producto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    cant_produc = models.IntegerField(default=0)


