from binascii import rledecode_hqx
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.

def studentLoginForm(request):
    if request.method =='POST':
        username = request.POST['email']
        password = request.POST['passwordd']
        print(username)
        print(password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(user.id)

            print("Correct Person")
            votinguser_details = VotingUsers.objects.filter(user_id=user.id)
            #data = votinguser_details.values()
            print(votinguser_details.values_list())
            #@Kiran, Aniket - Get this from Database
            
            if(TypeLogin == "head"):
                return render(request,'admin-updatevote.html')
            elif(TypeLogin == "student"):
                return render(request,'dashboard.html')
        else:
            print("Wrong Person")
            return render(request,'login-form.html')




    return render(request,'login-form.html')

def displayCollegeForm(request):
    if request.method == "POST":
       
        data_dict = request.POST

        college_name = data_dict['college_name']

        college = College.objects.create(
            college_name=college_name
            )

    college_details = College.objects.all()

    context = {"details":college_details}

    return render(request,'college-form.html', context)


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

    return render(request,'college-year.html', context)

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

    return render(request,'college-branch.html', context)

def displayStudentForm(request):
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

        student = Student.objects.create(
            name=name,email=email,
            prn_number=prn_number,password=password,
            conform_password = conform_password,
            college_id=college, branch_id=branch, year_id=year
            )

    student_details = Student.objects.all()
    college_details = College.objects.all()
    year_details = Year.objects.all()
    branch_details = Branch.objects.all()

    context = {"details":college_details,"years":year_details, 
    "departments":branch_details, "students":student_details }

    return render(request,'register-form.html', context)
 

def forgotPasswordForm(request):
    return render(request,'forgot-pwd.html')

def displayHomePage(request):
    return render(request,'home-page.html')

def displayDashboardPage(request):
    if request.method == "POST":

        data_dict = request.POST
        election = data_dict['election']
    
    election_details = Election.objects.all()

    context = {"elections":election_details}

    return render(request,'dashboard.html',context)

def displayNominee(request):
    if request.method == "POST":

        data_dict = request.POST
        nominee = data_dict['nominee']
        position = data_dict['position']
    
    nominee_details = Nominee.objects.all()
    position_details = Position.objects.all()

    context = {"positions":position_details,"nominees":nominee_details}

    return render(request,'nominee.html',context)

def displayResultPage(request):
    return render(request,'voting-result.html')

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
        
       

        admin = Authority.objects.create(
            name=name, email=email,
            mobile=mobile_number, college=college, 
            role=role, password=password,
            conform_password = conform_password,
            )

    admin_details = Authority.objects.all()

    context = {"authority":admin_details}

    return render(request,'admin-signup.html',context)

def adminLoginPage(request):
    return render(request,'admin-login.html')

def adminVoteUpdatePage(request):
    if request.method == "POST":
       
        data_dict = request.POST

        election_name = data_dict['election_name']

        election = Election.objects.create(
            election_name=election_name
            )

    election_details = Election.objects.all()

    context = {"elections":election_details}
    
    return render(request,'admin-updatevote.html',context)

def adminAddPostPage(request):
    if request.method == "POST":

        data_dict = request.POST
        election_post = data_dict['election_post']
        election = data_dict['election']

        position = Position.objects.create(
            election_post=election_post,
            election_id=election
            )

    position_details = Position.objects.all()
    election_details = Election.objects.all()

    context = {"elections":election_details,"positions":position_details}

    return render(request,'admin-addpost.html',context)

def adminAddNomineePage(request):
    if request.method == "POST":

        data_dict = request.POST
        nominee = data_dict['nominee']
        election = data_dict['election']
        position = data_dict['position']

        nominee = Nominee.objects.create(
            nominee=nominee,
            election_id=election,
            position_id=position
            )

    nominee_details = Nominee.objects.all()
    election_details = Election.objects.all()
    position_details = Position.objects.all()

    context = {"elections":election_details,"positions":position_details,"nominees":nominee_details}
    
    return render(request,'admin-addnominee.html',context)