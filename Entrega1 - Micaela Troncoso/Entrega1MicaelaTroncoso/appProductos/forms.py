from django import forms

class form_clientes (forms.Form):
    cuil_cuit = forms.CharField(max_length=40)
    nombre_apellido = forms.CharField(max_length=40)
    domicilio = forms.CharField(max_length=40)
    telefono = forms.IntegerField()

class form_facturas (forms.Form):
    fecha = forms.DateField()
    tipo = forms.CharField(max_length=1)
    nombre_apellido = forms.CharField(max_length=40)
    cuil_cuit = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    monto_sin_iva = forms.DecimalField(max_digits=15, decimal_places=2)
    iva = forms.DecimalField(max_digits=15, decimal_places=2)

class form_productos (forms.Form):
    producto = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=40)
    precio_sin_iva = forms.DecimalField(max_digits=15, decimal_places=2)
    iva = forms.DecimalField(max_digits=15, decimal_places=2)