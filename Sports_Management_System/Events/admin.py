from django.contrib import admin
from .models import event,rule,guest

#event model handling
class eventAdmin(admin.ModelAdmin):
    list_display = ('name','id','organiser')
admin.site.register(event,eventAdmin)

#rule model handling
class ruleAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_id')
admin.site.register(rule,ruleAdmin)

#guest model handling
class guestAdmin(admin.ModelAdmin):
    list_display = ("name","id_for_event")
admin.site.register(guest,guestAdmin)
