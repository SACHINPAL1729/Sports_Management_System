from django.contrib import admin
from .models import RegistrationData

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.core.mail import send_mail


# Register your models here.



# @admin.register(RegistrationData)


class RegistrationDataAdmin(admin.ModelAdmin):
    list_display = ('username','tournamentid', 'point')
    list_filter = ('tournamentid','sportname')
    actions = ['send_EMAIL']

    def send_EMAIL(self, request, queryset):
        if request.method=="POST":
            for i in queryset:
                print("Samyak Jain")
                if i.email:
                    send_mail('Arrey faaltu ki mail h, ignore kar', 'Aur Chacha kya maaze aa rhe', '1008jainsamyak1@gmail.com',[i.email], fail_silently=False)
                else:
                    self.message_user(request, "Mail sent successfully ") 
    send_EMAIL.short_description = "Send an email to selected users"

    
admin.site.register(RegistrationData,RegistrationDataAdmin)

