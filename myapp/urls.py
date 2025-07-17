from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("category/<slug:slug>/", views.blog_by_category, name="blog_by_category"),
    path("blog/create/", views.blog_create, name="blog_create"),
    path("blog/<int:blog_id>/comment/", views.add_comment, name="add_comment"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
]
