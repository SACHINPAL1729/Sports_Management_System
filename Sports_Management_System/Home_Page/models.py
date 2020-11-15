from django.db import models

# Create your models here.

class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    sportname = models.CharField(max_length=100)
    tournamentid = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    point = models.IntegerField(default=0)


    def __str__(self):
        return self.username
