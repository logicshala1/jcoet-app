from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# CharField: H # 1
# IntegerField: only numbers

class Bus(models.Model):
    vehicle_number = models.CharField(max_length=10)
    number_of_students = models.IntegerField(default=1)
    number_of_stops = models.IntegerField(default=1)

    def __str__(self):
        return self.vehicle_number

class Location(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
