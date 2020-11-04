from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from smartfields import fields
from datetime import date


class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    is_patient = models.BooleanField(
        default=True,
        help_text=_('Designates whether the user can log into the patient site.'),
    )
    is_doctor = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into the doctor site.'),
    )
    is_diagnostic = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into the diagnostic site.'),
    )

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    degrees = models.CharField(max_length=120)
    designation = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    specialization = models.CharField(max_length=80)
    address = models.CharField(max_length=150, null=True, blank=True)
    reg_no = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = fields.ImageField(
        upload_to='media/patient_image/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.get_full_name

    class Meta:
        order_with_respect_to = 'user'

    def save(self, *args, **kwargs):
        super(DoctorProfile, self).save(*args, **kwargs)


class PatientProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        related_name='patient_profile')
    doctor_reg_no = models.ForeignKey(DoctorProfile,
        on_delete=models.CASCADE,
        null=True,
        help_text="Enter doctor registration no")
    gender = models.CharField(max_length=1,
        choices=GENDER_CHOICES)
    dob = models.DateField(help_text="Enter your date of birth")
    height = models.DecimalField(null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Please input this in centimeters')
    weight = models.DecimalField(null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Please input this in kg')
    BP = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = fields.ImageField(
        upload_to='media/patient_image/',
        null=True,
        blank=True
    )

    class Meta:
        order_with_respect_to = 'user'

    def __str__(self):
        return self.user.get_full_name

    @property
    def get_bmi(self):
        if self.height == 0 or self.weight == 0:
            return 0
        else:
            height_in_meter = self.height / 100
            bmi = self.weight / (height_in_meter * height_in_meter)
            return format(float(bmi), ".1f")

    @property
    def get_calculated_age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age
