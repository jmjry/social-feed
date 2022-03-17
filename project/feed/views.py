from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView

class PostListView(ListView):
    model = Post
    template_name = "feed/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
