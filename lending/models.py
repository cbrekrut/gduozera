from django.db import models

# Create your models here.
class House(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=0)
	description = models.CharField(max_length=250, default='')
	image = models.ImageField(upload_to='uploads/house')


	def __str__(self):
		return self.name