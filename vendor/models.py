from django.db import models
# Create your models here.
from stdimage import StdImageField


class Vendor(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    type_of_business = models.CharField(max_length=150)
    company_owner_name = models.CharField(max_length=150)
    year_of_establishment = models.DateField()
    vat_id = models.IntegerField()
    # suplier_rating = models.IntegerField()
    likes = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class VendorImages(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='vendor_images'
    )
    banner_image = StdImageField(
        upload_to='media/images/vendor_images/',
        blank=True,
        null=True,
        editable=True,
    )
    optional_banner_image = StdImageField(
        upload_to='media/images/vendor_images/',
        blank=True,
        null=True,
        editable=True,
    )
    profile_image = StdImageField(
        upload_to='media/images/vendor_images/',
        blank=True,
        null=True,
        editable=True,
        variations={'thumbnail': (220, 140)}, delete_orphans=True
    )


class Account(models.Model):
    supplier_id = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='vendor_account'
    )
    account_name = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=150)
    account_holder_name = models.CharField(max_length=150)
    branch_name = models.CharField(max_length=150)
    branch_address = models.CharField(max_length=150)
    type_of_account = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class DeliveryMan(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    # account = models.ForeignKey(Account)
    join_ate = models.DateField()
    nid_or_passport_number = models.CharField(max_length=20)
    nid_or_passport_image = StdImageField(
        upload_to='media/images/delivery_man_images/',
        blank=True,
        null=True,
        editable=True,
        variations={'thumbnail': (220, 140)}, delete_orphans=True
    )
    drivingLicences = models.CharField(max_length=150)
    images = StdImageField(
        upload_to='media/images/delivery_man_images/',
        blank=True,
        null=True,
        editable=True,
        variations={'thumbnail': (220, 140)}, delete_orphans=True
    )



