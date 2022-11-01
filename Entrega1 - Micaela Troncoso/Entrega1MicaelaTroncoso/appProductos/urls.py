from django.urls import path
from appProductos.views import *

urlpatterns = [
    path('', home),
    path('clientes/', read_clientes),
    path('buscar_cliente/', buscar_cliente),
    path('create_cliente/', create_cliente),
    path('delete_cliente/<cliente_id>', delete_cliente),
    path('update_cliente/<cliente_id>', update_cliente),
    path('productos/', read_productos),
    path('buscar_producto/', buscar_producto),
    path('create_producto/', create_producto),
    path('delete_producto/<producto_id>', delete_producto),
    path('update_producto/<producto_id>', update_producto),
    path('facturas/', read_facturas),
    path('buscar_factura/', buscar_factura),
    path('create_factura/', create_factura),
    path('delete_factura/<factura_id>', delete_factura)
]