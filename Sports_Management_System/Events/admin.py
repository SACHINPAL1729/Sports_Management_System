from django.contrib import admin
from .models import event,rule,guest

# Register your models here.
@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    list_display = ('name','id','organiser')

admin.site.register(rule)

class guestAdmin(admin.ModelAdmin):
    list_display = ("name","id_for_event")

admin.site.register(guest,guestAdmin)

