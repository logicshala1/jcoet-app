from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('orderpage/',displayorderForm, name="orderpage"),
    path('ownerpage/',ownerPage, name="ownerpage"),
    path('login/',userLogin, name="user-login"),
]