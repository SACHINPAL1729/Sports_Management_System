from django.shortcuts import render
from .models import event,guest,rule
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
    # code to maintain events
    try:
        evnt = event.objects.get(pk=event_id)
    except event.DoesNotExist:
        raise Http404("Event does not exist")

    #code to manage guests
    guests = guest.objects.all()
    guest_for_this = []
    for i in guests:
        if i.id_for_event == event_id:
            guest_for_this.append(i)


    # code to maintain rules
    rules = rule.objects.all()
    rule_for_this = []
    for i in rules:
        if i.event_id == event_id:
            rule_for_this.append(i)

    exact_rules =[]
    temp = '';
    for i in rule_for_this:
        # for j in range(1,6):
            # temp = 'rule'+str(j)
            if i.rule1:
                exact_rules.append(i.rule1)
            if i.rule2:
                exact_rules.append(i.rule2)
            if i.rule3:
                exact_rules.append(i.rule3)
            if i.rule4:
                exact_rules.append(i.rule4)
            if i.rule5:
                exact_rules.append(i.rule5)

    pass_to_display = {'event_details' : evnt, 'guest_details' : guest_for_this,
    'rules':exact_rules}


    return render(request,'display.html',pass_to_display)
