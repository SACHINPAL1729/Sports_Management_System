from django.db import models

# Create your models here.
class feedback(models.Model):
    Name = models.CharField(max_length=200)
    event = models.CharField(max_length=150)
    event_id = models.IntegerField()
    email = models.EmailField()
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.Name