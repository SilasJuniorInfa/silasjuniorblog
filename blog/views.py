from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.views.generic import ListView, DetailView
from .forms import CommentForm


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Posts
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# Create your views here.
# def starting_page(request):
    #latest_posts = Posts.objects.all().order_by("-date")[:3]
    #return render(request, "blog/index.html",{
      #  "posts" : latest_posts})



class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Posts
    ordering = ["-date"]
    context_object_name = "all_posts"
    

# def all_posts(request):
    #all_posts = Posts.objects.all().order_by("-date")
    #return render(request, "blog/all-posts.html", {
     #   "all_posts": all_posts})


#def posts_detail(request, slug):
    #post_detail = get_object_or_404(Posts, slug=slug) #the rights its argument of function, the left of model
    #return render(request, "blog/post-detail.html", {
        #"post":post_detail,
        #
        # 
        # 
#"post_tags":post_detail.tags.all()

class PostsDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Posts
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context