from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import context

# Create your views here.

def register(request):
    form = UserCreationForm()
    context = ("form": form)
    return render(request, "users/register.html", context)