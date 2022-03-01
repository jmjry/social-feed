from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "feed/home.html", context)
