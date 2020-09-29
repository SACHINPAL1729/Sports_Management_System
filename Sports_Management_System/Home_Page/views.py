from django.shortcuts import render

def home(request):
    return render(request, 'Home_Page/index.html')
