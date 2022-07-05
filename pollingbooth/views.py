from django.shortcuts import render
from .models import *
# Create your views here.
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
 
def studentLoginForm(request):
    return render(request,'login-form.html')

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
    return render(request,'nominee.html')

def displayResultPage(request):
    return render(request,'voting-result.html')

def adminSignupPage(request):
    return render(request,'admin-signup.html')

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

        post = Position.objects.create(
            election_post=election_post,
            election_id=election
            )

    position_details = Position.objects.all()
    election_details = Election.objects.all()

    context = {"elections":election_details,"positions":position_details}

    return render(request,'admin-addpost.html',context)

def adminAddNomineePage(request):
    return render(request,'admin-addnominee.html')