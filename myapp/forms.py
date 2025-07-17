from django import forms
from .models import Category, Blog, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body", "image", "is_active", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "category": forms.Select(
                attrs={"class": "form-select"}
            ),  # este es el desplegable
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text"
        ]  # Solo el texto del comentario, el user y blog se asignan en la vista
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Escribe tu comentario aquí...",
                }
            ),
        }
        labels = {
            "text": "Comentario",
        }
