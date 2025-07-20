# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, AvatarForm
from .models import Avatar
from django.http import Http404


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required  # type: ignore
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")


@login_required
def update_profile(request):
    user_form = UserUpdateForm(instance=request.user)
    avatar_form = AvatarForm()

    try:
        avatar = request.user.avatar
        avatar_form = AvatarForm(instance=avatar)
    except Avatar.DoesNotExist:
        pass

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        avatar_form = AvatarForm(
            request.POST, request.FILES, instance=getattr(request.user, "avatar", None)
        )

        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar = avatar_form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect("home")

    return render(
        request,
        "accounts/update_profile.html",
        {"user_form": user_form, "avatar_form": avatar_form},
    )


def user_profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        avatar = getattr(user, "avatar", None)
    except User.DoesNotExist:
        raise Http404("Usuario no encontrado")

    return render(
        request, "accounts/user_profile.html", {"profile_user": user, "avatar": avatar}
    )
