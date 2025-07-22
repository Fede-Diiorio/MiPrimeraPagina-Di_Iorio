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
    path("blogs/search/", views.blog_search, name="blog_search"),
    path("category/<slug:slug>/", views.blog_by_category, name="blog_by_category"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "categories/create/", views.CategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "category/<int:category_id>/edit/",
        views.CategoryUpdateView.as_view(),
        name="edit_category",
    ),
    path(
        "category/<int:category_id>/delete/",
        views.CategoryDeleteView.as_view(),
        name="delete_category",
    ),
    path("comment/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path(
        "comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),
    path("about-me/", views.about_me, name="about_me"),
]
