from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from datetime import datetime
# Create your views here.
from django.shortcuts import render
from .models import *

def mainPage(request):
    return render(request,"user-ui.html")

def displayorderForm(request):
    if request.method == "POST":
        print("GOT THE DATA")
        print(request.POST)
        data_dict = request.POST
        print("Name_Of_Student ",data_dict['Name_Of_Student'])
    
    return render (request,'owner-page.html')    

def adminCanteen(request):
    return render(request,"adminpage.html")

def menu(request):
    menu_items = MenuItems.objects.all()

    context = {"items":menu_items}
    return render(request,'menu.html', context)

def messages(request):
    messages = FeedbackMessage.objects.order_by('-date').all()

    context = {"messages":messages}
    return render(request,'feedback_messages.html', context)


def addItem(request):
    if request.method == "POST":
        name = request.POST['item']
        rate = request.POST['rate']
        image = request.FILES.get('image',None)

        menu_item = MenuItems.objects.create(name=name,rate=rate)

        if image:
            media_name = str(name)+".jpg"
            menu_item.image.save(content=image, name=media_name, save=False)						
            menu_item.save()

    return render(request, 'owner-page.html')

def userLogin(request):
    if request.method == "POST":
        college_id = request.POST['college_id']
        password = request.POST['password']

        if UserDetails.objects.filter(college_id=college_id, password=password).exists():
            user = UserDetails.objects.filter(college_id=college_id, password=password).first()
            request.session['user'] = user.id

            if user.is_admin:
                return redirect('admin')
            else:
                return redirect('main-page')

    return render(request,"form_login.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        dob = request.POST['dob']
        college_id = request.POST['college_id']
        password = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']

        user = UserDetails.objects.create(
            username=username, date_of_birth=dob, password=password,
            college_id=college_id, mobile=mobile, email=email
            )

        if user:
            return redirect("login")

    return render(request,"form_created_account.html")

def adminregister(request):
    if request.method == "POST":
        username = request.POST['username']
        dob = request.POST['dob']
        college_id = request.POST['college_id']
        password = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']

        user = UserDetails.objects.create(
            username=username, date_of_birth=dob, password=password,
            college_id=college_id, mobile=mobile, email=email,
            is_admin=True
            )

        if user:
            return redirect("login")

    return render(request,"form_created_account.html")

def feedback(request):
    if request.method == "POST":
        print("GOT THE DATA")
        print(request.POST)
        data_dict = request.POST

        first_name = data_dict['firstname']
        last_name = data_dict['lastname']
        feedback = data_dict['feedback']

        FeedbackMessage.objects.create(name=first_name+' '+last_name, message = feedback, date=datetime.now())


    return render (request,'feedback.html')