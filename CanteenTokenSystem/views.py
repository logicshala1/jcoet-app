from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displaylogin(request):
    name="nitin",
    CanteenTokenSystem={
        "menu":{
            "name":"lunch",
            "name":"Dinner",
            "name":"coldrinks",
            "name":"Nasta",
        }
    }
    context = {"display_name":name,"CanteenTokenSystem":CanteenTokenSystem}
    return render(request,"login.html",context)


def home(request):
    return render(request,"home.html")

def displayregistration(request):
    return HttpResponse(request, "registration.html",context)

def displayorder(request):
    return render(request, "order.html",context)


