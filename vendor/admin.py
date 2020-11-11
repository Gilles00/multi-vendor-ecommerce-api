from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Vendor)
class Vendor(admin.ModelAdmin):
    list_display = ['name','address','company_name','mobile']


@admin.register(VendorImages)
class VendorImages(admin.ModelAdmin):
    list_display = ['vendor','profile_image']

@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ['account_name','bank_name','branch_name']

@admin.register(DeliveryMan)
class DeliveryMan(admin.ModelAdmin):
    list_display = ['name','address','phone']