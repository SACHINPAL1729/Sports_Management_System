from django.contrib import admin
from .models import *

# Register your models here.

class notif_modelAdmin(admin.ModelAdmin):
	list_display = ['heading','subject']

admin.site.register(notif_model,notif_modelAdmin)