from django.db import models
from product.models import Order

# Create your models here.


class ServiceMan(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    nid_or_pass = models.CharField(max_length=150)
    license_plate_number = models.CharField(max_length=150)
    license = models.CharField(max_length=150)



class DeliveryService(models.Model):
    service_name = models.CharField(max_length=150)
    company_details = models.TextField()
    service_man_id = models.ForeignKey(ServiceMan, on_delete=models.CASCADE)


class DeliveryDetails(models.Model):
    delivery_service_id = models.ForeignKey(DeliveryService, on_delete=models.CASCADE)
    delivery_pickup_time = models.TimeField()
    delivery_receive_time = models.TimeField()
    is_active = models.BooleanField()
    delivery_orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    service_man_id = models.ForeignKey(ServiceMan, on_delete=models.CASCADE)


