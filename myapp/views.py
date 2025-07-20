from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Blog, Comment
from .forms import CategoryForm, BlogForm, CommentForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden


def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_staff)(view_func)
    return decorated_view_func


def home_view(request):
    return render(request, "myapp/home.html")


# <--- CATEGORIAS --->
def category_list(request):
    categories = Category.objects.all()
    return render(request, "myapp/categories.html", {"categories": categories})


@admin_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "myapp/category_form.html", {"form": form})


@admin_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "myapp/edit_category.html", {"form": form})


@admin_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "myapp/delete_category.html", {"category": category})


# <--- BLOGS --->
def blog_list(request):
    blogs = Blog.objects.filter(is_active=True).order_by("-date")
    return render(request, "myapp/blog_list.html", {"blogs": blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.all().order_by("-date")  # type: ignore

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.blog = blog
                comment.save()
                return redirect("blog_detail", blog_id=blog.id)  # type: ignore
        else:
            return redirect("login")
    else:
        form = CommentForm()

    return render(
        request,
        "myapp/blog_detail.html",
        {
            "blog": blog,
            "comments": comments,
            "form": form,
        },
    )


def blog_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=category, is_active=True)
    return render(
        request, "myapp/blog_by_category.html", {"category": category, "blogs": blogs}
    )


@login_required
def blogs_by_user(request, username):
    user = get_object_or_404(User, username=username)
    blogs = Blog.objects.filter(user=user).order_by("-date")
    return render(
        request,
        "myapp/blogs_by_user.html",
        {
            "blogs": blogs,
            "blog_owner": user,
        },
    )


@admin_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("blog_list")
    else:
        form = BlogForm()
    return render(request, "myapp/blog_form.html", {"form": form})


@admin_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blog_detail", blog_id=blog.id)  # type: ignore
    else:
        form = BlogForm(instance=blog)
    return render(request, "myapp/edit_blog.html", {"form": form})


@admin_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect("blog_list")
    return render(request, "myapp/delete_blog.html", {"blog": blog})


# <--- COMENTARIOS --->
@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect("blog_detail", blog_id=blog.id)  # type: ignore
    else:
        form = CommentForm()
    return render(request, "myapp/add_comment.html", {"form": form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("blog_detail", blog_id=comment.blog.id)  # type: ignore
    else:
        form = CommentForm(instance=comment)

    return render(
        request,
        "myapp/edit_comment.html",
        {
            "form": form,
            "comment": comment,
        },
    )


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")
    if request.method == "POST":
        comment.delete()
        messages.success(request, "El comentario ha sido eliminado correctamente.")
        return redirect("blog_detail", blog_id=comment.blog.id)  # type: ignore

    return render(request, "myapp/delete_comment.html", {"comment": comment})
