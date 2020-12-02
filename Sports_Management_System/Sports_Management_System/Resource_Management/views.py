from django.shortcuts import render
from .models import Resource
# Create your views here.

def Resource_Management(request):
    a = Resource.objects.all()
    resource = []
    for i in a:
        temp = {
            'name' : i.name,
            'available' : i.available,
            'requirement' : i.requirement,
        }
        resource.append(temp)
    
    context = {'resource' : resource,}

    return render(request, 'resource.html', context)
