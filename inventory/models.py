from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from smartfields import fields
from stdimage import StdImageField
from vendor.models import Vendor
from customer.models import CustomerProfile
from delivery.models import *
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_email = models.EmailField(max_length=50, null=True)
    supplier_phone = models.CharField(max_length=15, null=True)
    supplier_address = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.supplier_name


# product category
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    alternative_name = models.CharField(max_length=150)
    descriptions = models.TextField()
    icon = StdImageField(
        upload_to='media/images/category_images/' + str(name) + '/',
        blank=True,
        null=True,
        editable=True,
    )
    image = StdImageField(
        upload_to='media/images/category_images/' + str(name) + '/',
        blank=True,
        null=True,
        editable=True,
    )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


# product sub-category
class ProductSubCategory(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        related_name='category',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    alternative_name = models.CharField(max_length=150)
    descriptions = models.TextField()
    icon = StdImageField(
        upload_to='media/images/category_images/' + str(name) + '/',
        blank=True,
        null=True,
        editable=True,
    )
    image = StdImageField(
        upload_to='media/images/category_images/' + str(name) + '/',
        blank=True,
        null=True,
        editable=True,
    )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class ProductWarranty(models.Model):
    WARRANTY_CHOICES = (
        ('R', 'Replacement'),
        ('S', 'Service'),
        ('O', 'Other'),
    )
    INTERVAL_CHOICES = (
        ('dd', 'Day'),
        ('mm', 'Month'),
        ('yy', 'Year'),
    )
    type = models.CharField(max_length=1, choices=WARRANTY_CHOICES)
    interval = models.CharField(max_length=2, choices=INTERVAL_CHOICES)
    limit = models.IntegerField(null=True, blank=True)
    conditions = models.TextField(max_length=500)

    def __str__(self):
        return self.type + '--' + self.interval + '--' + str(self.limit)


# product Information
class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    supplier_id = models.ForeignKey(
        Supplier,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(validators=[MinValueValidator(0)])
    sock_quantity = models.IntegerField()
    sub_category = models.ForeignKey(
        ProductSubCategory,
        on_delete=models.CASCADE,
        related_name='product_sub_category',
        null=True
    )
    category = models.ForeignKey(
        ProductSubCategory,
        on_delete=models.CASCADE,
        related_name='product_category',
        blank=True,
        null=True
    )
    alternative_names = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )
    description = models.TextField()
    warranty_id = models.ForeignKey(
        ProductWarranty,
        on_delete=models.SET_NULL,
        null=True,
        default=None)
    warranty_limit = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=None,
        null=True)
    minimum_order_quantity = models.IntegerField(validators=[MinValueValidator(1)])
    maximum_order_quantity = models.IntegerField(validators=[MinValueValidator(1)])
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# product Images
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = StdImageField(
        upload_to='media/images/product_images/' + str(product) + '/',
        blank=True,
        null=True,
        editable=True,
        variations={'thumbnail': (220, 140)}, delete_orphans=True
    )


# product Purchased
class ProductPurchased(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    selling_price = models.DecimalField()
    buying_price = models.DecimalField()
    purchase_date = models.DateField()
    additional_field = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


# Product Review
class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(User, on_delete= models.SET('Unknown'))
    review = models.CharField(max_length=150)
    is_active = models.CharField(max_length=150)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


# discount
class Discount(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_discount'
    )
    conditions = models.CharField(max_length=200)
    discount_percentage = models.IntegerField(null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


# Coupon
class Coupon(models.Model):
    is_active = models.BooleanField(default=False)
    coupon_code = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.IntegerField(null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    limit = models.CharField(max_length=70)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


# Custom offer
class CustomOffer(models.Model):
    supplier = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    offer_description = models.TextField()
    title = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

