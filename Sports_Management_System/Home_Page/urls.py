from django.urls import path
from Home_Page import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='add'),
]
