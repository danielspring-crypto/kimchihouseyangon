from django.db import models

# Create your models here.
class Order(models.Model):
	name = models.CharField(max_length=255)
	count = models.IntegerField()
	phone = models.CharField(max_length=255)
	address = models.TextField()
	cost = models.CharField(max_length=255)
	delivery_fees = models.CharField(max_length=255)
	paid = models.BooleanField(default=False)
	date = models.DateField()

	def __str__(self):
		return self.name 
