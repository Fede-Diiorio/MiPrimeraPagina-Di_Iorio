from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    image = models.ImageField(upload_to="avatares")

    def __str__(self) -> str:
        return f"Avatar de {self.user.username}"
