from django.contrib import admin
from .models import *


@admin.register(CustomerAddress)
class CustomerAddress(admin.ModelAdmin):
    list_display = ['user','city', 'house_number']


@admin.register(CustomerProfile)
class CustomerProfile(admin.ModelAdmin):
    list_display = ['name','phone']

