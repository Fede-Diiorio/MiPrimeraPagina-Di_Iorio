from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Blog, Comment
from .forms import CategoryForm, BlogForm, CommentForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q


def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_staff)(view_func)
    return decorated_view_func


def home_view(request):
    return render(request, "myapp/home.html")


def about_me(request):
    return render(request, "myapp/about-me.html")


# <--- CATEGORIAS --->
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff  # type: ignore

    def handle_no_permission(self):
        return HttpResponseForbidden("No tienes permisos para acceder a esta vista.")


class CategoryListView(ListView):
    model = Category
    template_name = "myapp/categories.html"
    context_object_name = "categories"


class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "myapp/category_form.html"
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "myapp/edit_category.html"
    pk_url_kwarg = "category_id"
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    model = Category
    template_name = "myapp/delete_category.html"
    context_object_name = "category"
    pk_url_kwarg = "category_id"
    success_url = reverse_lazy("category_list")


# <--- BLOGS --->
def blog_list(request):
    query = request.GET.get("q", "")

    blogs = Blog.objects.all().order_by("-date")

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        )

    return render(
        request,
        "myapp/blog_list.html",
        {
            "blogs": blogs,
        },
    )


def blog_search(request):
    query = request.GET.get("q", "")
    category_id = request.GET.get("category", "")

    blogs = Blog.objects.all().order_by("-date")

    if query:
        blogs = blogs.filter(title__icontains=query)
    if category_id:
        blogs = blogs.filter(category__id=category_id)

    categories = Category.objects.all()

    return render(
        request,
        "myapp/blog_search_results.html",
        {
            "blogs": blogs,
            "query": query,
            "selected_category": category_id,
            "categories": categories,
        },
    )


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
