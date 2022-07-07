from django.shortcuts import render
from .models import *

def displayBusForm(request):
    if request.method == "POST":
        print("GOT THE DATA")
        print(request.POST)
        data_dict = request.POST
        print("The vechile number is ",data_dict['vehicle_number'])


        vehicle_number = data_dict['vehicle_number']
        number_of_students = data_dict['number_of_students']
        number_of_stops = data_dict['number_of_stops']

        bus = Bus.objects.create(
            vehicle_number=vehicle_number, 
            number_of_students=number_of_students,
            number_of_stops=number_of_stops
            )


    bus_details = Bus.objects.all()

    context = {"details":bus_details}

    return render(request,'bus-form.html', context)

def studentForm(request):
    if request.method == "POST":

        data_dict = request.POST


        name = data_dict['name']
        email = data_dict['email']
        year = data_dict['year']
        branch = data_dict['branch']
        mobile = data_dict['mobile']
        bus = data_dict['bus']

        print(bus)

        student = Students.objects.create(
            name=name, year=year, 
            mobile=mobile,branch=branch, email=email,
            bus_id=bus
            )

    student_details = Students.objects.all()
    bus_details = Bus.objects.all()

    context = {"details":bus_details,"students":student_details}

    return render(request,'student-form.html', context)