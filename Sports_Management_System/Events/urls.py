from django.urls import path
from . import views
urlpatterns = [
    path('', views.Events, name='Events'),
    path('<int:event_id>/',views.display_event,name='display_event'),
]
