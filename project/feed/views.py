from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "feed/home.html", context)
