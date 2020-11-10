from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from smartfields import fields
from stdimage import StdImageField

from inventory.models import Product
from vendor.models import Vendor
from customer.models import CustomerProfile, CustomerAddress
from delivery.models import *
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    ORDER_STATUS = (
        ('PLACED', 'Order Placed'),
        ('RECEIVED', 'Order Received'),
        ('SHIPPING', 'Order is on the way'),
        ('DONE', 'Order Completed'),
        ('CANCELED', 'Order Canceled'),
    )

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='customer_order'
    )
    is_active = models.BooleanField()
    order_tracking_number = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    order_note = models.TextField(max_length=500, null=True, blank=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PLACED')
    delivery_address = models.ForeignKey(
        CustomerAddress,
        related_name='shipping_address',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.pk} - {self.customer} - {self.order_status}"

    @property
    def order_amount(self):
        return 0


class OrderDetails(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='ordered_product'
    )
    sku = models.CharField(max_length=200)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    unit_price = models.DecimalField()

    @property
    def count_item_total(self):
        return self.unit_price * self.quantity

    def save(self, *args, **kwargs):
        if self.unit_price is None:
            self.unit_price = self.product.price
        super(OrderDetails, self).save(*args, **kwargs)


class PaymentDetails(models.Model):
    PAYMENT_METHOD = (
        ('BKASH', 'Order Placed'),
        ('ROCKET', 'Order Received'),
        ('CARD', 'Order is on the way'),
        ('CASHON', 'Order Completed'),
    )
    PAYMENT_STATUS = (
        ('PENDING', 'Payment is pending'),
        ('PAID', 'Payment received'),
        ('PARTIAL', 'Partial payment received'),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_payment'
    )
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)
    amount_paid = models.DecimalField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.amount_paid is None or self.amount_paid is 0:
            self.amount_paid = self.order.order_amount
        super(PaymentDetails, self).save(*args, **kwargs)
