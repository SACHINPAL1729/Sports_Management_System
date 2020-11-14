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


# class rule(models.Model):
#     id= models.OneToOneField(
#     event,
#     on_delete=models.CASCADE,
#     )
#     event_id = models.IntegerField()
#     rule1 = models.TextField(default='')
#     rule2 = models.TextField(default='')
#     rule3 = models.TextField(default='')
#     rule4 = models.TextField(default='')
#     rule5 = models.TextField(default='')
#
    # def __str__(self):
        # return self.


class rule(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=50,default='')
    rule1 = models.TextField(default='')
    rule2 = models.TextField(default='',blank=True)
    rule3 = models.TextField(default='',blank=True)
    rule4 = models.TextField(default='',blank=True)
    rule5 = models.TextField(default='',blank=True)

    def __str__(self):
        return str(self.event_name)

class guest(models.Model):
    id_for_event = models.IntegerField()
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
