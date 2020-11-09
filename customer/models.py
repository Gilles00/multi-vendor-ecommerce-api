from django.db import models
from smartfields import fields
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
from stdimage import StdImageField






class CustomerAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_address')
    zip_code = models.CharField(max_length=50)
    area = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    house_number = models.CharField(max_length=50, null=True)
    flat_number = models.CharField(max_length=50, null=True)
    floor_number = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name


class CustomerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_profile')
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    image = StdImageField(
        upload_to='media/images/customer_images/',
        blank=True,
        null=True,
        editable=True,
    )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name


