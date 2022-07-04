from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('loginform/',displayLoginForm, name="login-form"),
    path('registerform/',displayRegisterForm, name="register-form"),
    path('voteridregisterform/',VoterIdForm, name="voter-id-form"),
]
