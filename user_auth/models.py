from django.contrib.auth.models import User
from django.db import models

# Create your models here.

ROLE_CHOICES = (
        ('Delivery', 'Delivery Man'),
        ('Vendor', 'Vendor'),
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
    )
class UserRole(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_role'
    )
    user_role = models.CharField(choices=ROLE_CHOICES)

