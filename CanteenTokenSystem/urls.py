from django.urls import path
from .views import*
urlpatterns=[
    path('home/',home, name="homepage"),
    path('login/',displaylogin,name="displaylogin"),
    path('registration/',displayregistration,name="displayregistration"),
    path('order/',displayorder,name="displayorder"),
]