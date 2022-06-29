from django.shortcuts import render


def displayBusForm(request):
    return render(request,'bus-form.html')