from django.contrib import admin

# Register your models here.

from .models import Client, Order, Product

register_models = [Client, Order, Product]

admin.site.register(register_models)
