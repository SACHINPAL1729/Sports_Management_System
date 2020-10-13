from django.urls import path
from . import views
app_name='Feedback'
urlpatterns = [
    path('', views.home, name='home'),
]
