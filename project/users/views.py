from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def set_form_fields(form):
    form.fields["username"].help_text = ""
    form.fields["password1"].help_text = ""
    form.fields["password2"].label = "Confirm Password"
    form.fields["password2"].help_text = ""

def register(request):
    if request.method == "POST": 
       form = UserRegisterForm(request.POST)
       set_form_fields(form)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get("username")
           messages.success(request,f'Account created for {username}. You can now login.')
           return redirect("login")
    else:  
        form = UserRegisterForm()
        set_form_fields(form)
    context = {"form": form}
    return render(request, "users/register.html", context)