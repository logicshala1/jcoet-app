from django.db import models

# Create your models here.
#charField: H # 1
#IntegerField: only numbers

class order(models.Model):
    Name_Of_Student = models.CharField(max_length=25)
    Student_ID_Number = models.IntegerField(20)
    Name_Of_Item = models.CharField(max_length=10)
    Quantity_Of_Item = models.IntegerField(500)
    
    def __str__(self):
        return self.Name_Of_Student
    
class option(models.Model):
    Extra_Item = models.CharField(max_length=500)
    Beverages_Name = models.CharField(max_length=25)
    Quantity_Of_Beverages = models.IntegerField(100)