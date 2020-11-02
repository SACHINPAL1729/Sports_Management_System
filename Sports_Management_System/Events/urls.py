from django.urls import path
from . import views
urlpatterns = [
    path('', views.Events, name='Events'),
]
