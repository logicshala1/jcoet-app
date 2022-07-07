from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class VotingDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=500,blank=True,default='student')
    userCreated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.user.username}'
class ElectionUsers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    typeOfLogin = models.CharField(max_length=300,blank=True,default='student')

    def __str__(self):
        return self.user.username

class VotingUsers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    typeLogin = models.CharField(max_length=400,blank=True,default='student')

    def __str__(self):
        return self.user.username
        
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
    typeLogin = models.CharField(max_length=100,default='student')
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
    branch = models.ManyToManyField(Branch)
    def __str__(self):
        return self.election_name

class Position(models.Model):
    election_post = models.CharField(max_length=50)
    election = models.ForeignKey(Election,on_delete=models.CASCADE)

    def __str__(self):
        return self.election_post

class Authority(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    typeLogin = models.CharField(max_length=100,default='admin')
    college = models.CharField(max_length=500)
    role = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    conform_password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Nominee(models.Model):
    nominee = models.CharField(max_length=500)
    election = models.ForeignKey(Election,on_delete=models.CASCADE)
    position = models.ForeignKey(Position,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nominee

class Result(models.Model):
    
    candidate = models.ForeignKey(Nominee,on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=500)

    def __str__(self):
        return self.voter_name
