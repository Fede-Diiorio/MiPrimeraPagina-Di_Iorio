from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, update_profile
from .forms import CustomLoginForm


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html", authentication_form=CustomLoginForm
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", update_profile, name="update_profile"),
]
