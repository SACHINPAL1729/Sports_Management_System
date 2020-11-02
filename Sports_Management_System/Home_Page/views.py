from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import RegistrationData

def home(request):
    return render(request, 'home.html')

def register(request):
    context = {
        "form":RegistrationForm
    }
    return render(request, 'register.html',context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister =  RegistrationData(username = form.cleaned_data['username'],
        sportname =form.cleaned_data['sportname'],
        tournamentid =form.cleaned_data['tournamentid'],
        phone = form.cleaned_data['phone'],
        email = form.cleaned_data['email']
        )
        myregister.save()
    return render(request, 'thanks.html')
    # return redirect('Events')
    # later fix redirect('home') why not working
