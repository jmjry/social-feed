from django.shortcuts import render


posts = [
    {
        'author': 'Jake',
        'title': 'Post 1',
        'content': 'This is the first post',
        'date_posted': '22nd Feb 2022'
    },

    {
        'author': 'Brad',
        'title': 'Post 2',
        'content': 'This is the second post',
        'date_posted': '23rd Feb 2022'
    }
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, "feed/home.html", context)
