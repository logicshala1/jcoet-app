from django.shortcuts import render

# Create your views here.
def displayLoginForm(request):
    return render(request,'login-form.html')

def displayRegisterForm(request):
    return render(request,'register-form.html')

def VoterIdForm(request):
    return render(request,'voter-id-form.html')


