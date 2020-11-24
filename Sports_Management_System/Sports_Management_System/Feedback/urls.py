from django.urls import path
from . import views
app_name='Feedback'

urlpatterns = [
    path('', views.Feedback, name='Feedback'),
    path('save_feed/',views.Save,name="save_feed"),
]
