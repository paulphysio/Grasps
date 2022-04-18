from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, contact_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':

        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi, {username}, you have created an account in succesfully')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    } 
    return render(request, "Grasps/signup.html", context)

def contact_sender(request):
    if request.method == 'POST':

        contactform = contact_form(request.POST or None)
        if contactform.is_valid():
            contactform.save(commit = True)
            contactform = contact_form()

            name = contactform.cleaned_data.get('name')
            messages.success(request, f'Hi, {name}, your message have been sent succesfully')
            return redirect('home')
    else:
        contactform = contact_form()
    context = {
        'contactform':contactform
    } 
    return render(request, "Grasps/home.html", context)

    
    

def home(response):
    
    return render(response, "Grasps/home.html", {})

@login_required
def profile(response):
    
    return render(response, "Grasps/profile.html", {})
