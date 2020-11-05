from django.db import models
from customer.models import Images
# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    typeOfBusiness = models.CharField(max_length=150)
    companyOwnerName = models.CharField(max_length=150)
    yearOfEstablish = models.DateField()
    vat = models.IntegerField()
    dttm = models.DateTimeField()
    rating = models.IntegerField()
    like = models.IntegerField()
    images = models.ForeignKey(Images)


class Account(models.Model):
    supplier = models.ForeignKey(Supplier)
    accountName = models.CharField(max_length=150)
    bankName = models.CharField(max_length=150)
    accountHolderName = models.CharField(max_length=150)
    branchName = models.CharField(max_length=150)
    branchAddress = models.CharField(max_length=150)
    typeOfAccount = models.CharField(max_length=50)
    dttm = models.DateTimeField()


class DeliveryMan(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    account = models.ForeignKey(Account)
    joinDate = models.DateField()
    nidOrPassport = models.CharField(max_length=150)
    drivingLicences = models.CharField(max_length=150)
    images = models.ForeignKey(Images)


class Banners(models.Model):
    supplier = models.ForeignKey(Supplier)
    images = models.ForeignKey(Images)
    priority = models.IntegerField()