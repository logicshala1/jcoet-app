"""
Author- Kiran Kamble
Date created- 2022-06-30
"""

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Election_Level)
admin.site.register(College_Election_Position)
admin.site.register(College_Election_Nominee)
admin.site.register(Election_of_Department)
admin.site.register(Department_Election_Position)
admin.site.register(Department_Election_Nominee)
admin.site.register(College_Election_Voter)
admin.site.register(Department_Election_Voter)
