# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(label="¿Este usuario es staff?", required=False)

    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["image"]
