from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('collegeform/',displayCollegeForm, name="college-form"),
    path('collegeyear/',displayYear, name="college-year"),
    path('collegebranch/',displayBranch, name="college-branch"),
    path('registerform/',displayStudentForm, name="register-form"),
    path('loginform/',studentLoginForm, name="login-form"),
    path('forgotpassword/',forgotPasswordForm, name="forgot-password"),
    path('homepage/',displayHomePage, name="home-page"),
    path('dashboard/',displayDashboardPage, name="dash-board"),
    path('nominee/',displayNominee, name="nominee"),
    path('adminsignup/',adminSignupPage, name="admin-signup"),
    
    
]