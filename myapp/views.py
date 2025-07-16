from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Blog
from .forms import CategoryForm, BlogForm, CommentForm
from django.contrib.auth.decorators import user_passes_test, login_required


def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_superuser)(view_func)
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


@admin_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = BlogForm()
    return render(request, "myapp/blog_form.html", {"form": form})


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
