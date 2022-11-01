from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from appProductos.forms import *
from appProductos.models import *
# Create your views here.

def home (request):
    return render(request, "home.html")

def buscar_cliente (request):
    if request.GET['cuil_cuit']:
        cuil_cuit = request.GET['cuil_cuit']
        busc_clientes = Clientes.objects.filter(cuil_cuit__icontains = cuil_cuit)
        return render(request, "clientesCRUD/read_clientes.html", {"busc_clientes":busc_clientes})
    else:
        respuesta= "Introduce el Cuil/Cuit"
    return HttpResponse(respuesta)


def read_clientes (request=None):
    clientes = Clientes.objects.all()
    return render(request, "clientesCRUD/read_clientes.html", {"clientes":clientes})

def delete_cliente (request, cliente_id):
    cliente = Clientes.objects.get(id= cliente_id)
    cliente.delete()
    return redirect('/appProductos/clientes')

def update_cliente (request, cliente_id):
    cliente = Clientes.objects.get(id = cliente_id)

    if request.method == 'POST':
        formulario = form_clientes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cliente.cuil_cuit = informacion['cuil_cuit']
            cliente.nombre_apellido = informacion['nombre_apellido']
            cliente.domicilio = informacion['domicilio']
            cliente.telefono = informacion['telefono']
            cliente.save()
            return redirect('/appProductos/clientes')

    else:
        formulario = form_clientes(initial={'cuil_cuit': cliente.cuil_cuit, 'nombre_apellido': cliente.nombre_apellido, 'domicilio': cliente.domicilio, 'telefono': cliente.telefono})
    
    return render(request, "clientesCRUD/update_cliente.html", {"formulario":formulario})

def create_cliente (request):
    if request.method == 'POST':
        cliente = Clientes(cuil_cuit = request.POST['cuil_cuit'], nombre_apellido = request.POST['nombre_apellido'], domicilio = request.POST['domicilio'], telefono = request.POST['telefono'])
        cliente.save()
        return redirect('/appProductos/clientes')
    return render(request, "clientesCRUD/create_cliente.html")

def buscar_factura (request):
    if request.GET['numero']:
        numero = request.GET['numero']
        busc_facturas = Facturas.objects.filter(numero__icontains = numero)
        return render(request, "facturasCRUD/read_facturas.html", {"busc_facturas":busc_facturas})
    else:
        respuesta= "Introduce el nº de factura"
    return HttpResponse(respuesta)

def read_facturas (request=None):
    facturas = Facturas.objects.all()
    return render(request, "facturasCRUD/read_facturas.html", {"facturas":facturas})

def delete_factura (request, factura_id):
    factura = Facturas.objects.get(id= factura_id)
    factura.delete()
    return redirect('/appProductos/facturas')

def create_factura (request):
    if request.method == 'POST':
        factura = Facturas(fecha = request.POST['fecha'], tipo = request.POST['tipo'], nombre_apellido = request.POST['nombre_apellido'], cuil_cuit = request.POST['cuil_cuit'], numero = request.POST['numero'], monto_sin_iva = request.POST['monto_sin_iva'], iva = request.POST['iva'])
        factura.save()
        return redirect('/appProductos/facturas')

    return render(request, "facturasCRUD/create_factura.html")
    
def buscar_producto (request):
    if request.GET['producto']:
        producto = request.GET['producto']
        busc_productos = Productos.objects.filter(producto__icontains = producto)
        return render(request, "productosCRUD/read_productos.html", {"busc_productos":busc_productos})
    else:
        respuesta= "Introduce el nombre del producto"
    return HttpResponse(respuesta)

def read_productos (request=None):
    productos = Productos.objects.all()
    return render(request, "productosCRUD/read_productos.html", {"productos":productos})

def delete_producto (request, producto_id):
    producto = Productos.objects.get(id= producto_id)
    producto.delete()
    return redirect('/appProductos/productos')
    
def update_producto (request, producto_id):
    producto = Productos.objects.get(id = producto_id)

    if request.method == 'POST':
        formulario = form_productos(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            producto.producto = informacion['producto']
            producto.descripcion = informacion['descripcion']
            producto.precio_sin_iva = informacion['precio_sin_iva']
            producto.iva = informacion['iva']
            producto.save()
            return redirect('/appProductos/productos')

    else:
        formulario = form_productos(initial={'producto': producto.producto, 'descripcion': producto.descripcion, 'precio_sin_iva': producto.precio_sin_iva, 'iva': producto.iva})
    
    return render(request, "productosCRUD/update_producto.html", {"formulario":formulario})

def create_producto (request):
    if request.method == 'POST':
        producto = Productos(producto = request.POST['producto'], descripcion = request.POST['descripcion'], precio_sin_iva = request.POST['precio_sin_iva'], iva = request.POST['iva'])
        producto.save()
        return redirect('/appProductos/productos')

    return render(request, "productosCRUD/create_producto.html")