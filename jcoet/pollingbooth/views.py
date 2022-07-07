from binascii import rledecode_hqx
from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.

def displayHomePage(request):
    return render(request,'home-page.html')

def loginDashboardPage(request):
    return render(request,'login-dashboard.html')

def adminSignupPage(request):
    if request.method == "POST":

        data_dict = request.POST
        name = data_dict['name']
        email = data_dict['email']
        mobile_number = data_dict['mobile_number']
        college = data_dict['college']
        role = data_dict['role']
        password = data_dict['password']
        conform_password = data_dict['conform_password']
        
       
        print("Trying to create")
        #TODO - Kiran - To check if database is updated or not
        user = Authority.objects.create(
            name=name, email=email,
            mobile=mobile_number, college=college, 
            role=role, password=password,
            conform_password = conform_password,
            typeLogin="admin"
            )
            
        admin_details = Authority.objects.all()

        if user:
            return redirect("add-college")

    return render(request,'admin-signup.html')

def adminLoginPage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if Authority.objects.filter(email=email, password=password).exists():
            user = Authority.objects.filter(email=email, password=password).first()
            request.session['user'] = user.id

            if user.typeLogin:
                return redirect('add-college')
            else:
                return redirect('polling-home-page')

    
    return render(request,'admin-login.html')
    

def studentSignupForm(request):
    if request.method == "POST":
        data_dict = request.POST
        name = data_dict['name']
        email = data_dict['email']
        prn_number = data_dict['prn_number']
        password = data_dict['password']
        conform_password = data_dict['conform_password']
        college = data_dict['college']
        year = data_dict['year']
        branch = data_dict['branch']
        

        user = Student.objects.create(
            name=name,email=email,typeLogin="student",
            prn_number=prn_number,password=password,
            conform_password = conform_password,
            college_id=college, branch_id=branch, year_id=year,
            
            )
        #TODO Kiran - type as student and change Student to Authority
    student_details = Student.objects.all()
    college_details = College.objects.all()
    year_details = Year.objects.all()
    branch_details = Branch.objects.all()

    # context = {"details":college_details,"years":year_details, 
    # "departments":branch_details, "students":student_details }

    if user:
        return redirect("dash-board")


    return render(request,'register-form.html')    

def studentLoginForm(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if Student.objects.filter(email=email, password=password).exists():
            user = Student.objects.filter(email=email, password=password).first()
            request.session['user'] = user.id

            if user.typeLogin:
                return redirect('dash-board')
            else:
                return redirect('polling-home-page')

    
    return render(request,'admin-login.html')

def displayDashboardPage(request):
    if request.method == "POST":

        data_dict = request.POST
        election = data_dict['election']
    
    election_details = Election.objects.all()

    context = {"elections":election_details}

    return render(request,'dashboard.html',context)

def displayNominee(request):

    electionID = request.GET.get('election')
    
    
    if request.method == "POST":
        data_dict = request.POST
        nominee = data_dict['nominee']
        position = data_dict['position']    
    
    nominee_details = Nominee.objects.all().filter(election=electionID)
    election_name = Election.objects.all().filter(id=electionID)
    
    context = {"nominees":nominee_details,"election_name":election_name[0]}
    
    return render(request,'nominee.html',context)

def displayResultPage(request):
    electionID = request.GET.get('election')
    
    if request.method == "POST":
        data_dict = request.POST
        nominee = data_dict['nominee']
        position = data_dict['position']
        
    
    nominee_details = Nominee.objects.all().filter(election=electionID)
    election_name = Election.objects.all().filter(id=electionID)
    context = {"nominees":nominee_details,"election_name":election_name[0]}

def displayCollegeForm(request):
    if request.method == "POST":
       
        data_dict = request.POST
        college_name = data_dict['college_name']
        college = College.objects.create(
            college_name=college_name
            )

    college_details = College.objects.all()

    context = {"details":college_details}

    return render(request,'admin-addclg.html', context)


def displayYear(request):
    if request.method == "POST":
        data_dict = request.POST
        year = data_dict['year']
        college = data_dict['college']

        year = Year.objects.create(
            year=year,
            college_id=college
            )

    year_details = Year.objects.all()
    college_details = College.objects.all()

    context = {"details":college_details,"years":year_details}

    return render(request,'admin-addyear.html', context)

def displayBranch(request):
    if request.method == "POST":
        data_dict = request.POST
        branch = data_dict['branch']
        college = data_dict['college']

        branch = Branch.objects.create(
            branch=branch,
            college_id=college
            )

    branch_details = Branch.objects.all()
    college_details = College.objects.all()

    context = {"details":college_details,"departments":branch_details}

    return render(request,'admin-addbranch.html', context)

def adminAddElectionPage(request):
    if request.method == "POST":
       
        data_dict = request.POST
        print("PRINTING DATA_DICT")
        print(data_dict)
        election_name = data_dict['election_name']
        print(data_dict.getlist('checkbox-branches'))
        print("============================")
        election = Election.objects.create(
            election_name=election_name
        )
        print(data_dict['checkbox-branches'])
        print("=--------------------")
        for i in data_dict.getlist('checkbox-branches'):
            election.branch.add(int(i))
            print(i)
            
            

    branch_details = Branch.objects.all()

    election_details = Election.objects.all()
    election_branches = election_details[0].branch.all()
    print(election_details)
    print("DEBUG...")
    context = {"elections":election_details,"branches":branch_details}
    
    return render(request,'admin-addelection.html',context)

def adminAddNomineePage(request):
    if request.method == "POST":

        data_dict = request.POST
        nominee = data_dict['nominee']
        election = data_dict['election']
        print(election)
        print("------****------")
        nominee = Nominee.objects.create(
            nominee=nominee,
            election_id=int(election),
            )

    nominee_details = Nominee.objects.all()
    election_details = Election.objects.all()

    context = {"elections":election_details,"nominees":nominee_details}
    
    return render(request,'admin-addnominee.html',context)

