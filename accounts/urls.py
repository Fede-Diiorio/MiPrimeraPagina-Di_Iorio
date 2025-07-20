# accounts/urls.py
from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    update_profile,
    user_profile_view,
)

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),  # type: ignore
    path("update/", update_profile, name="update_profile"),
    path("profile/<str:username>/", user_profile_view, name="user_profile"),
]
