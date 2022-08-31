from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm



def welcome(request):
    return HttpResponse("<h1><center>Welcome to Login System</cenetr></h1>")


# login view
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})