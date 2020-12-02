from django.shortcuts import render
from .models import Resource
# Create your views here.

def Resource_Management(request):
    a = Resource.objects.all()
    resource = []
    for i in a:
        xyz = 0
        if(i.available < i.requirement):
            xyz = i.requirement-i.available
        temp = {
            'name' : i.name,
            'available' : i.available,
            'requirement' : i.requirement,
            'purchase' : xyz,
        }
        resource.append(temp)
    
    context = {'resource' : resource,}

    return render(request, 'resource.html', context)
