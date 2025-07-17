from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("blog/create/", views.blog_create, name="blog_create"),
    path("blog/<int:blog_id>/comment/", views.add_comment, name="add_comment"),
    path("blog/<int:blog_id>/edit/", views.edit_blog, name="edit_blog"),
    path("blog/<int:blog_id>/delete/", views.delete_blog, name="delete_blog"),
    path("blog/<str:username>/", views.blogs_by_user, name="blogs_by_user"),
    path("category/<slug:slug>/", views.blog_by_category, name="blog_by_category"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("category/<int:category_id>/edit/", views.edit_category, name="edit_category"),
    path(
        "category/<int:category_id>/delete/",
        views.delete_category,
        name="delete_category",
    ),
]
