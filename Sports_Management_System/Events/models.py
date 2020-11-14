from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
    organiser = models.CharField(max_length=100)
    about = models.TextField(default='')
    # rules = models.TextField(default='')
    # csvfile = models.FileField(upload_to='csvfile_for_guest/')
    contact = models.TextField(default='')
    details = models.TextField(default='')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'


class rule(models.Model):
    event_id = models.IntegerField()
    rule1 = models.TextField(default='')
    rule2 = models.TextField(default='')
    rule3 = models.TextField(default='')
    rule4 = models.TextField(default='')
    rule5 = models.TextField(default='')

#     def __str__(event):
#         return event.name
      
class guest(models.Model):
    id_for_event = models.IntegerField()
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
