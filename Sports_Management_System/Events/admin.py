from django.contrib import admin
from .models import event,guest

# Register your models here.
class eventAdmin(admin.ModelAdmin):
    list_display = ("name","id","organiser")

admin.site.register(event,eventAdmin)

class guestAdmin(admin.ModelAdmin):
    list_display = ("name","id_for_event")

admin.site.register(guest,guestAdmin)