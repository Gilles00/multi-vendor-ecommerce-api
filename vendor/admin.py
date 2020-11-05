from django.contrib import admin
from .models import Supplier, Account, DeliveryMan, Banners

# Register your models here.
@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display = ['name','address','company','contact','email','mobile','telephone','typeOfBusiness','companyOwnerName','yearOfEstablish','vat','dttm','rating','like','images']


@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ['supplier','accountName','bankName','accountHolderName','branchName','branchAddress','typeOfAccount','dttm']

@admin.register(DeliveryMan)
class DeliveryMan(admin.ModelAdmin):
    list_display = ['name','address','phone','email','account','joinDate','nidOrPassport','drivingLicences', 'images']


@admin.register(Banners)
class Banners(admin.ModelAdmin):
    list_display = ['supplier', 'images', 'priority']
