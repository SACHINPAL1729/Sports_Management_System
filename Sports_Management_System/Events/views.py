from django.shortcuts import render
from .models import event,guest
import time
from django.utils import timezone
# Create your views here.
def Events(request):

    events = event.objects.all()

    upcoming = []
    past = []

    for i in events:
        details = {
            'event_id' : i.id,
            'event_name' : i.name,
            'organiser' : i.organiser,
            'time' : i.timestamp,
        }

        current = str(timezone.now())
        if(current<str(i.timestamp)):
            upcoming.append(details)
        else:
            past.append(details)


    context = {'uevents' : upcoming, 'pevents' : past}

    return render(request, 'Events.html', context)


def display_event(request,event_id):
    try:
        evnt = event.objects.get(pk=event_id)
    except event.DoesNotExist:
        raise Http404("Event does not exist")

    #code to manage guest
    guests = guest.objects.all()
    guest_for_this = []
    for i in guests:
        if i.id_for_event == event_id:
            guest_for_this.append(i)

    
    pass_to_display = {'event_details' : evnt, 'guest_details' : guest_for_this}

    return render(request,'display.html',pass_to_display)