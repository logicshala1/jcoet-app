from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('adminsignup/',adminSignupPage, name="admin-signup"),
    path('collegeform/',displayCollegeForm, name="college-form"),
    path('collegeyear/',displayYear, name="college-year"),
    path('collegebranch/',displayBranch, name="college-branch"),
    path('electionupdate/',adminVoteUpdatePage, name="election-update"),
    path('electionpost/',adminAddPostPage, name="election-post"),   
    path('addcandidate/',adminAddNomineePage, name="add-candidate"),
    path('registerform/',displayStudentForm, name="register-form"),
    path('loginform/',studentLoginForm, name="login-form"),
    path('forgotpassword/',forgotPasswordForm, name="forgot-password"),
    path('',displayHomePage, name="polling-home-page"),
    path('dashboard/',displayDashboardPage, name="dash-board"),
    path('nominee/',displayNominee, name="nominee"),
    path('votingresult/',displayResultPage, name="voting-result"),
    
    
    
]