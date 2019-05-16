from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class flights(models.Model):
	flightid= models.CharField(max_length=100)
	starttime=models.DateTimeField()
	endtime=models.DateTimeField()
	price=models.FloatField()
	startplace=models.CharField(max_length=255)
	endplace=models.CharField(max_length=255)
	volume=models.IntegerField(default=1000)

	class Meta:
		db_table="flights"
