from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',homeDisplay,name="home-display"),
    path('team',teamDisplay,name='team-display'),
    path('apps',appDisplay,name='apps-display')
]