from django.contrib import admin
from .models import event,rule

# Register your models here.
@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    list_display = ('name','id','organiser')

admin.site.register(rule)
# admin.site.register(event, eventAdmin)
