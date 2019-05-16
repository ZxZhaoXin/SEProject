from django.db import models


class Flight(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    check_in_time = models.DateTimeField(max_length=50)
    check_out_time = models.DateTimeField(max_length=50)
    price = models.PositiveIntegerField()
    class Meta:
        db_table = "flight"

class People(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    class Meta:
        db_table ="people"


    


