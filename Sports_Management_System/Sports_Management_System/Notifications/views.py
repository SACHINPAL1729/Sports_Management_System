from django.shortcuts import render
from .models import *

# Create your views here.

def notif(request):
	updates = notif_model.objects.all()

	crnt_notif = []

	for i in updates:
		crnt_notif.append(i)

	pass_to_notif = {
		'crnt_notif':crnt_notif,
	}

	return render(request,'notifications.html',pass_to_notif)