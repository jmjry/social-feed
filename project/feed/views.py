from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = "feed/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
