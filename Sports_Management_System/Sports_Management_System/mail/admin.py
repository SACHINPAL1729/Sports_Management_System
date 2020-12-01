from django.contrib import admin
from Home_Page.models import RegistrationData
from .models import MailText

# Register your models here.

class MailTextAdmin(admin.ModelAdmin):
    list_display = ('event_id','subject','send_it')

admin.site.register(MailText,MailTextAdmin)