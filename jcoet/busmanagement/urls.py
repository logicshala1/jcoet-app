from django.urls import path
# import functions from the views files
from .views import *

urlpatterns = [
    path('<path-to-function>/',function-name, name="<url-name>"),
]