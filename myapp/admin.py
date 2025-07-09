from django.contrib import admin

# Register your models here.

from .models import Product, Category

register_models = [Product, Category]

admin.site.register(register_models)
