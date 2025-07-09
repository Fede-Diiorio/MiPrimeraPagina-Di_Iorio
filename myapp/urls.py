from django.urls import path
from .views import (
    home_view,
    product_list,
    product_create,
    category_list,
    category_create,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("productos/", product_list, name="product_list"),
    path("productos/crear/", product_create, name="product_create"),
    path("categorias/", category_list, name="category_list"),
    path("categorias/crear/", category_create, name="category_create"),
]
