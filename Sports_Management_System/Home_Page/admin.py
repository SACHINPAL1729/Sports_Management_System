from django.contrib import admin
from .models import RegistrationData

# Register your models here.

class RegistrationDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'tournamentid',)
    list_filter = ('tournamentid'),

admin.site.register(RegistrationData,RegistrationDataAdmin)
