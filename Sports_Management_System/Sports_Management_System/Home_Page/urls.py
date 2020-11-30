from django.urls import path
from Home_Page import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='add'),
    path('addUser/',views.addUser,name='addUser'),
    # path('',views.SendUserEmails,name='email')
]
