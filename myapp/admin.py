from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, Blog, CustomUser

register_models = [Product, Category, Blog]

admin.site.register(CustomUser, UserAdmin)
