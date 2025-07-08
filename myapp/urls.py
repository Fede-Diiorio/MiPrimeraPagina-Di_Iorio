from django.urls import path
from .views import (
    product_list,
    client_list,
    order_list,
    home_view,
    create_product,
    create_client,
    create_order,
    product_detail,
    search_product,
    search_client,
    search_order,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("productos/", product_list, name="productos"),
    path("productos/nuevo/", create_product, name="crear_producto"),
    path("productos/buscar", search_product, name="buscar_producto"),
    path("productos/<int:product_id>/", product_detail, name="detalle_producto"),
    path("clientes/", client_list, name="clientes"),
    path("clientes/nuevo/", create_client, name="crear_cliente"),
    path("clientes/buscar", search_client, name="buscar_clientes"),
    path("ordenes/", order_list, name="ordenes"),
    path("ordenes/nueva/", create_order, name="crear_orden"),
    path("ordenes/buscar", search_order, name="buscar_ordenes"),
]
