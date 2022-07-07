from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('',displayHomePage, name="polling-home-page"),
    path('logindashboard/',loginDashboardPage, name="login-dashboard"),
    path('adminsignup/',adminSignupPage, name="admin-signup"),
    path('adminlogin/',adminLoginPage, name="admin-login"),
    path('registerform/',studentSignupForm  , name="register-form"),
    path('loginform/',studentLoginForm, name="login-form"),
    path('addcollege/',displayCollegeForm, name="add-college"),
    path('addyear/',displayYear, name="add-year"),
    path('addbranch/',displayBranch, name="add-branch"),
    path('addelection/',adminAddElectionPage, name="add-election"),  
    path('addnominee/',adminAddNomineePage, name="add-nominee"),    
    path('dashboard/',displayDashboardPage, name="dash-board"),
    path('nominee/',displayNominee, name="nominee"),
    path('result/',displayNewResultPage, name="new-voting-result"),
    path('votingresult/',displayResultPage, name="voting-result"),
    
    
    
]