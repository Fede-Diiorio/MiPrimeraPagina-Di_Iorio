from django.contrib import admin

# Register your models here.

from .models import Product, Category, Blog

register_models = [Product, Category, Blog]

admin.site.register(register_models)
