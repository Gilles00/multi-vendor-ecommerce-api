from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ServiceMan)
class ServiceMan(admin.ModelAdmin):
    list_display = ['name','phone','nid_or_pass']


@admin.register(DeliveryService)
class DeliveryService(admin.ModelAdmin):
    list_display = ['service_name','company_details','service_man']


@admin.register(DeliveryDetails)
class DeliveryDetails(admin.ModelAdmin):
    list_display = [ 'order', 'delivery_service', 'service_man']
