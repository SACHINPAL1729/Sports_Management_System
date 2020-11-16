from django.db import models
from django.db.models import Model
# from phonenumber_field.modelfields import PhoneNumberField
# from phone_field import PhoneField

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
    link = models.URLField(default='',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'

class rule(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=50,default='')
    rule1 = models.TextField(default='')
    rule2 = models.TextField(default='',blank=True)
    rule3 = models.TextField(default='',blank=True)
    rule4 = models.TextField(default='',blank=True)
    rule5 = models.TextField(default='',blank=True)

    def __str__(self):
        return self.event_name


class guest(models.Model):
    id_for_event = models.IntegerField()
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class prize(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=100)
    first_prize = models.CharField(max_length=100)
    second_prize = models.CharField(max_length=100,default='',blank=True)
    third_prize = models.CharField(max_length=100,default='',blank=True)

    def __str__(self):
        return self.event_name

class contact(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=12)
    contact_email = models.EmailField(max_length=50,blank=True)

    def __str__(self):
        return self.contact_name

