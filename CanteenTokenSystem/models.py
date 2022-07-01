from django.db import models

# Create your models here.

class Canteen(models.Model):
    token_number=models.IntegerField(default=1)
    samosa= models.IntegerField(default=1)
    kachori=models.IntegerField(default=1)
    dosa=models.IntegerField(default=1)
    wadapav=models.IntegerField(default=1)
    pavbhaji=models.IntegerField(default=1)


    def __str__(self):
        return self.token_number
class students(models.Model):
    token_number=models.IntegerField(default=1)
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)

    def __str__(self):
        return self.token_number