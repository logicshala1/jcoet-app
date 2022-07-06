from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(College)
admin.site.register(Year)
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Election)
admin.site.register(Position)
admin.site.register(Authority)
admin.site.register(Nominee)
admin.site.register(ElectionUsers)