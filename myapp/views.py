from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Product, Client, Order
from .forms import ProductForm, ClientForm, OrderForm
from django.db.models import Q


def home_view(request: HttpRequest):
    return render(request, "home.html")


def product_list(request: HttpRequest):
    products = Product.objects.all()
    return render(request, "myapp/products.html", {"products": products})


def product_detail(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "myapp/product_detail.html", {"product": product})


def search_product(request: HttpRequest):
    query = request.GET.get("name", "")
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(
        request, "myapp/search_product.html", {"products": products, "query": query}
    )


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data["name"],
                price=form.cleaned_data["price"],
                description=form.cleaned_data["description"],
            )
            return redirect("productos")
    else:
        form = ProductForm()

    return render(request, "myapp/product_form.html", {"form": form})


def client_list(request: HttpRequest):
    clients = Client.objects.all()
    return render(request, "myapp/clients.html", {"clients": clients})


def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(
                name=form.cleaned_data["name"],
                lastname=form.cleaned_data.get("lastname", "Sin Apellido"),
                email=form.cleaned_data["email"],
            )
            return redirect("clientes")
    else:
        form = ClientForm()

    return render(request, "myapp/client_form.html", {"form": form})


def search_client(request: HttpRequest):
    query = request.GET.get("name", "")
    clients = (
        Client.objects.filter(Q(name__icontains=query) | Q(lastname__icontains=query))
        if query
        else []
    )
    return render(
        request, "myapp/search_clients.html", {"clients": clients, "query": query}
    )


def order_list(request: HttpRequest):
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "myapp/orders.html", {"orders": orders})


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(client=form.cleaned_data["client"])
            order.products.set(form.cleaned_data["products"])
            return redirect("ordenes")
    else:
        form = OrderForm()

    return render(request, "myapp/order_form.html", {"form": form})


from .models import Order


def search_order(request: HttpRequest):
    query = request.GET.get("name", "")
    orders = (
        Order.objects.filter(
            Q(client__name__icontains=query) | Q(client__lastname__icontains=query)
        )
        if query
        else []
    )
    return render(
        request, "myapp/search_orders.html", {"orders": orders, "query": query}
    )
