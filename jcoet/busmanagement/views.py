from django.shortcuts import render


def displayBusForm(request):
    if request.method == "POST":
        print("GOT THE DATA")
        print(request.POST)
        data_dict = request.POST
        print("The vechile number is ",data_dict['vehicle_number'])
        
    return render(request,'bus-form.html')