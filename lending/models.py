from django.db import models

# Create your models here.
class House(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=0)
	description = models.CharField(max_length=250, default='')
	image = models.ImageField(upload_to='uploads/house')


	def __str__(self):
		return self.name
	
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    main_img = models.ImageField(upload_to='uploads/service_images')

    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/service_images')

    def __str__(self):
        return f"Image for {self.service.name}"