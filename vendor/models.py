from django.db import models
# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    type_of_business = models.CharField(max_length=150)
    company_owner_name = models.CharField(max_length=150)
    year_of_establish = models.DateField()
    vat = models.IntegerField()
    dttm_stmp = models.DateTimeField()
    suplier_rating = models.IntegerField()
    likes = models.IntegerField()
    images = models.ForeignKey(Images)


class Account(models.Model):
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=150)
    account_holder_name = models.CharField(max_length=150)
    branch_name = models.CharField(max_length=150)
    branch_address = models.CharField(max_length=150)
    type_of_account = models.CharField(max_length=50)
    dttm_stmp = models.DateTimeField()


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