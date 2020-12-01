from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import RegistrationData
from Events.models import event
from django.utils import timezone

def home(request):
    events = event.objects.all()
    current_event = []

    for i in events:
        details = {
            'event_id' : i.id,
            'event_name' : i.name,
            'organiser' : i.organiser,
            'time' : i.timestamp,
        }

        current = str(timezone.now())
        if(current<str(i.timestamp_for_finish)):
            current_event.append(details)



    context = {'cevents' : current_event,}
    return render(request, 'home.html',context)

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


