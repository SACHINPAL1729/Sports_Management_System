from django.db import models

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    note = models.TextField(max_length=1000)
    requirement = models.IntegerField(default=0)


    def __str__(self):
        return self.name;