from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, CategoryForm


def home_view(request):
    return render(request, "myapp/home.html")


# Listar productos
def product_list(request):
    products = Product.objects.all()
    return render(request, "myapp/products.html", {"products": products})


# Crear producto
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "myapp/product_form.html", {"form": form})


# Listar categorías
def category_list(request):
    categories = Category.objects.all()
    return render(request, "myapp/categories.html", {"categories": categories})


def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "myapp/products_by_category.html",
        {"category": category, "products": products},
    )


# Crear categoría
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "myapp/category_form.html", {"form": form})
