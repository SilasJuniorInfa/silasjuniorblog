from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="initial-page"),
    path("posts/", views.posts, name="posts-page"),
    path( "posts/<slug:slug>/", views.posts_detail, name="post-detail-page"),  # /posts/my-first-blog <slug # permite só caracteres de strings e alguns caracteres validem a url sem contar os caracteres especiais
]
