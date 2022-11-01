from django.db import models

# Create your models here.


class Clientes (models.Model):
    cuil_cuit = models.CharField(max_length=40)
    nombre_apellido = models.CharField(max_length=40)
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Cuil/Cuit: {self.cuil_cuit}, Nombre: {self.nombre_apellido}, Domicilio: {self.domicilio}, Telefono: {self.telefono}."

class Facturas (models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=1)
    nombre_apellido = models.CharField(max_length=40)
    cuil_cuit = models.CharField(max_length=40)
    numero = models.IntegerField()
    monto_sin_iva = models.DecimalField(max_digits=15, decimal_places=2)
    iva = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Fecha: {self.fecha}, Factura: {self.tipo} nº {self.numero}, Nombre: {self.nombre_apellido} Cuil/Cuit: {self.cuil_cuit}, Monto s/Iva: {self.monto_sin_iva}, Iva: {self.iva}."

class Productos (models.Model):
    producto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    precio_sin_iva = models.DecimalField(max_digits=15, decimal_places=2)
    iva = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Producto: {self.producto}, Precio s/iva: {self.precio_sin_iva}, Iva: {self.iva}, Descripcion: {self.descripcion}."
