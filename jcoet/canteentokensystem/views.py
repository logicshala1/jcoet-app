from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *

def displayorderForm(request):
    if request.method == "POST":
        print("GOT THE DATA")
        print(request.POST)
        data_dict = request.POST
        print("Name_Of_Student ",data_dict['Name_Of_Student'])
    
    return render (request,'orderpage.html')    