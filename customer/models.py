from django.db import models



# Create your models here.

class Images(models.Model):
    images = models.ImageField()

class Address(models.Model):
    zipCode = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    houseNumber = models.CharField(max_length=50)
    houseName = models.CharField(max_length=50)
    flatNumber = models.CharField(max_length=50)
    floorNumber = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Customer(models.Model):
    name = models.CharField(max_length=150)
    address = models.ForeignKey(Address)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    dttm = models.DateField()
    images = models.ForeignKey(Images)


