from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeDisplay(request):
    return render(request,'home.html')

def teamDisplay(request):
    return render(request,'team.html')

def appDisplay(request):
    return render(request,'app-display.html')