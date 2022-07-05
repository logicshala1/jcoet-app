from django.db import models

# Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=80)

    def __str__(self):
        return self.college_name

class Year(models.Model):
    year = models.CharField(max_length=50)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return self.year

class Branch(models.Model):
    branch = models.CharField(max_length=50)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return self.branch

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    prn_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    conform_password = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name

class Election(models.Model):
    election_name = models.CharField(max_length=50)

    def __str__(self):
        return self.election_name

class Position(models.Model):
    election_post = models.CharField(max_length=50)
    election = models.ForeignKey(Election,on_delete=models.CASCADE)

    def __str__(self):
        return self.election_post