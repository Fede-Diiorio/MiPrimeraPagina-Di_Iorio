from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    create_blog,
    home_view,
    product_list,
    product_create,
    category_list,
    category_create,
    products_by_category,
    blog_list,
    blog_detail,
    register_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("productos/", product_list, name="product_list"),
    path("productos/crear/", product_create, name="product_create"),
    path("categorias/", category_list, name="category_list"),
    path("categorias/crear/", category_create, name="category_create"),
    path(
        "productos/categoria/<slug:slug>/",
        products_by_category,
        name="products_by_category",
    ),
    path("blog/", blog_list, name="blog_list"),
    path("blog/crear/", create_blog, name="blog_create"),
    path("blog/<int:blog_id>/", blog_detail, name="blog_detail"),
    path("login/", LoginView.as_view(template_name="myapp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", register_view, name="register"),
]
