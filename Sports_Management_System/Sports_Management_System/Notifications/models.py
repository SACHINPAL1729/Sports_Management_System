from django.db import models

# Create your models here.

class notif_model(models.Model):
	heading = models.CharField(max_length=255)
	subject = models.TextField(default='')

	def __str__(self):
		return self.heading