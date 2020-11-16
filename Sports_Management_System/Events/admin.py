from django.contrib import admin
from .models import *

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

#Prize model handling
class prizeAdmin(admin.ModelAdmin):
    list_display = ("event_name","event_id","first_prize")
admin.site.register(prize,prizeAdmin)

#Contact  handling models
class contactAdmin(admin.ModelAdmin):
    list_display = ("contact_name","contact_phone","event_name","event_id")
admin.site.register(contact,contactAdmin)
