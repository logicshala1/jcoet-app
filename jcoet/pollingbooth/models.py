"""
Author- Kiran Kamble
Date created- 2022-06-30
"""

from django.db import models

# Create your models here.
class Election_Level(models.Model):
    election_level = models.CharField(max_length=20)

    def __str__(self):
        return self.election_level

class College_Election_Position(models.Model):
    election_position = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)

    def __str__(self):
        return self.election_position

class College_Election_Nominee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    unique_id = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)
    election_position = models.ForeignKey(College_Election_Position,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name


class Election_of_Department(models.Model):
    election_of_branch = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)

    def __str__(self):
        return self.election_of_branch


class Department_Election_Position(models.Model):
    election_position = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)
    election_of_branch = models.ForeignKey(Election_of_Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.election_position
    
class Department_Election_Nominee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    unique_id = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)
    election_of_branch = models.ForeignKey(Election_of_Department,on_delete=models.CASCADE)
    election_position = models.ForeignKey(Department_Election_Position,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name

class College_Election_Voter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    prn_number = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)
    election_position = models.ForeignKey(College_Election_Position,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name

class Department_Election_Voter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    prn_number = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    election_level = models.ForeignKey(Election_Level,on_delete=models.CASCADE)
    election_of_branch = models.ForeignKey(Election_of_Department,on_delete=models.CASCADE)
    election_position = models.ForeignKey(College_Election_Position,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name