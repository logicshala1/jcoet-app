from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('orderpage/',displayorderForm, name="orderpage"),
    path("register/",register,name="register"),
    path("add-new-admin/",adminregister,name="register-admin"),
    path('login/',userLogin, name="login"),
    path('menu/',menu, name="menu"),
    path('add-item/',addItem,name="add-item"),
    path('canteen-admin/',adminCanteen,name="admin"),
<<<<<<< HEAD
    path('feedback/',feedback,name="feedback"),
=======
    path('main/',mainPage,name="main-page")
>>>>>>> 53ee6bffed93772d3f90534569837295eef93a46
]