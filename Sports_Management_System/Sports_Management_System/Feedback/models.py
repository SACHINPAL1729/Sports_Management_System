from django.db import models

# Create your models here.
class feedback(models.Model):
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    event = models.CharField(max_length=150)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.customer_name