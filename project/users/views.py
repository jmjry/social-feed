from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST": 
       form = UserCreationForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data.get("username")
    else:  
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "users/register.html", context)