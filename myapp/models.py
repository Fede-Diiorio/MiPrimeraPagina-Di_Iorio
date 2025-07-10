# myapp/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    image = models.TextField(default="Sin-Imagen", help_text="URL de la imagen")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    description = models.TextField()
    image = models.TextField(default="Sin-Imagen")
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title


class CustomUser(AbstractUser):
    # Agregá más campos si querés, por ejemplo:
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.username
