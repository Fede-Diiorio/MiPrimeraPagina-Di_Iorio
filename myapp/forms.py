from django import forms
from .models import Client, Product


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Nombre del producto",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    price = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        required=True,
        label="Descripción",
    )


class ClientForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    lastname = forms.CharField(
        max_length=50,
        required=False,
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )


class OrderForm(forms.Form):
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        label="Cliente",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        label="Productos",
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
    )
