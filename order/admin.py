from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['order_tracking_number','customer', 'delivery_address']


@admin.register(OrderDetails)
class OrderDetails(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity','unit_price']



@admin.register(PaymentDetails)
class PaymentDetails(admin.ModelAdmin):
    list_display = ['order', 'payment_method', 'amount_paid']

