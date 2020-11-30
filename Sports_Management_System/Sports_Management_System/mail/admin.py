from django.contrib import admin
from Home_Page.models import RegistrationData

# Register your models here.

class MailAdmin(admin.ModelAdmin):
    list_display = ('username','tournamentid', 'point')
    list_filter = ('tournamentid','sportname')

# admin.site.register(RegistrationData,MailAdmin)