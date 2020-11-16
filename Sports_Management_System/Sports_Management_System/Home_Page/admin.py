from django.contrib import admin
from .models import RegistrationData

# Register your models here.



# @admin.register(RegistrationData)
class RegistrationDataAdmin(admin.ModelAdmin):
    list_display = ('username','tournamentid', 'point')
    list_filter = ('tournamentid','sportname')

admin.site.register(RegistrationData,RegistrationDataAdmin)

