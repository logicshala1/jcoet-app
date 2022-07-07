from django.db import models
# college_id: ADM123
#password: admin123


# Create your models here.
#charField: H # 1
#IntegerField: only numbers
class UserDetails(models.Model):
    username = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    college_id = models.CharField(max_length=7)
    mobile = models.IntegerField()
    email = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=0)

    def __str__(self):
        return self.username

class MenuItems(models.Model):
    name = models.CharField(max_length=50)
    rate = models.FloatField(default=0)
    image = models.ImageField(upload_to="menu")

    def __str__(self):
        return self.name

class order(models.Model):
    name_of_student = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    name_of_item = models.ManyToManyField(MenuItems)
    quantity_of_item = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    token_number = models.CharField(max_length=8)

    def __str__(self):
        return self.name_of_student
    
