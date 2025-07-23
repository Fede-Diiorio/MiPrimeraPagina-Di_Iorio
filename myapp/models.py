# myapp/models.py

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    image = models.TextField(default="Sin-Imagen", help_text="URL de la imagen")

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(
        upload_to="myapp/blog_images/",
        help_text="Imagen del blog",
    )
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="blogs"
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.user.username}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.blog.title} - {self.user.username} - {self.date}"
