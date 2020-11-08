from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from smartfields import fields
from stdimage import StdImageField
from vendor.models import Supplier
from customer.models import CustomerProfile
from delivery.models import DeliveryDetails


# product category
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    alternative_name = models.CharField(max_length=150)
    descriptions = models.TextField()
    icon = StdImageField(
        upload_to='media/images/category_images/' + name + '/',
        blank=True,
        null=True,
        editable=True,
    )
    image = StdImageField(
        upload_to='media/images/category_images/' + name + '/',
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
        upload_to='media/images/category_images/' + name + '/',
        blank=True,
        null=True,
        editable=True,
    )
    image = StdImageField(
        upload_to='media/images/category_images/' + name + '/',
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
        return self.type+'--'+self.interval+'--'+str(self.limit)


# product Information
class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    supplier_id = models.ForeignKey(Supplier,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    price = models.DecimalField(validators=[MinValueValidator(0)])
    sock_quantity = models.IntegerField()
    sub_category = models.ForeignKey(ProductSubCategory,
        on_delete=models.CASCADE,
        related_name='product_sub_category',
        null=True)
    category = models.ForeignKey(ProductSubCategory,
        on_delete=models.CASCADE,
        related_name='product_category',
        blank=True,
        null=True)
    alternative_names = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(validators=[MinValueValidator(0)],default=0)
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
        upload_to='media/images/product_images/'+product.category.name+'/',
        blank=True,
        null=True,
        editable=True,
        variations={'thumbnail': (220, 140)}, delete_orphans=True
    )


# product Purchased
class ProductPurchased(models.Model):
    product_id = models.ForeignKey(Product, on_delete=mode)
    supplier_id = models.ForeignKey(Supplier)
    price = models.IntegerField()
    buying_price = models.IntegerField()
    date = models.DateField()
    additional_field = models.CharField(max_length=150)


# Product Review
class Review(models.Model):
    product_id = models.ForeignKey(Product)
    customer_id = models.ForeignKey(Customer)
    review = models.CharField(max_length=150)
    is_active = models.CharField(max_length=150)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


# discount
class Discount(models.Model):
    product_id = models.ForeignKey(Product)
    discount = models.CharField(max_length=200)
    discount_percentage = models.IntegerField()
    discount_amount = models.IntegerField()
    is_active = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()


# Coupon
class Coupon(models.Model):
    product_id = models.ForeignKey(Product)
    coupon_code = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.ForeignKey(Discount)
    limit = models.CharField(max_length=70)


# Warranty
class Warranty(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    duration = models.IntegerField()
    policy = models.TextField()


# Custom offer
class Custom_offer(models.Model):
    supplier = models.ForeignKey(Supplier)
    products_id = models.ForeignKey(Product)
    offer_description = models.TextField()


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_amount = models.IntegerField()
    order_placement_date_time = models.DateTimeField()
    is_active = models.BooleanField()
    order_tracking_number = models.IntegerField()
    delivey_details_id = models.ForeignKey(DeliveryDetails, on_delete=models.CASCADE)


class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=200)
    quantity = models.IntegerField()
