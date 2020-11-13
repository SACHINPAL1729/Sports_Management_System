from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
    organiser = models.CharField(max_length=100)
    about = models.TextField(default='')
    rules = models.TextField(default='')
    csvfile = models.FileField(upload_to='csvfile_for_guest/')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'

class guest(models.Model):
    id_for_event = models.IntegerField()
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
