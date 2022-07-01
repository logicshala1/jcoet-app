from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayorder(request):
    name="nitin",
    sample={
        "menu":{
            "name":"lunch",
            "name":"Dinner",
            "name":"coldrinks",
            "name":"Nasta",
        }
    }
    context = {"display_name":name,"sample":sample}
    return render(request,"order.html",context)