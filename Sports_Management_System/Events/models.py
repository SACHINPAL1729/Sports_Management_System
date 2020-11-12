from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
    organiser = models.CharField(max_length=100)
    # about = models.CharField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'events'
