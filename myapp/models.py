# myapp/models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50, default="Sin Apellido")
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.name} {self.lastname}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        productos = ", ".join([p.name for p in self.products.all()])
        return f"Pedido #{self.pk} de {self.client.name} {self.client.lastname} | Producto: {productos}"
