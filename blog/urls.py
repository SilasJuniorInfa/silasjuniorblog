from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostsDetailView.as_view(), name="post-detail-page"),  # /posts/my-first-blog <slug # permite só caracteres de strings e alguns caracteres validem a url sem contar os caracteres especiais
]

