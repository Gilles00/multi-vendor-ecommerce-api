from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from vendor.models import Supplier
from customer.models import Customer
from delivery.models import DeliveryDetails




# product category
class Category(models.Model):
    name = models.CharField(max_length=150)
    alternative_name = models.CharField(max_length=150)
    descriptions = models.TextField()
    dttm_stmp = models.DateTimeField()
    def __str__(self):
        return self.name


# product sub-category
class Sub_category(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=150)
    alternative_name = models.CharField(max_length=150)
    descriptions = models.TextField()
    dttm_stmp = models.DateTimeField()

    def __str__(self):
        return self.name



#product Information
class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    supplier_id = models.ForeignKey(Supplier)
    price = models.IntegerField()
    sock_quantity = models.IntegerField()
    category_id = models.ForeignKey(Category)
    alternative_names = models.CharField(max_length=150)
    isActive = models.BooleanField()
    dttm_stm = models.DateTimeField()
    views = models.IntegerField()
    description = models.TextField()
    warranty_id = models.IntegerField(null=True)
    minimum_order_quantity = models.IntegerField()
    maximum_order_quantity = models.IntegerField()

    def __str__(self):
        return self.name



# product Images
class ProductImages(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_field = models.ImageField()

# product Percest
class Product_purchased(models.Model):
    product_id = models.ForeignKey(Product)
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
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

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
    sku  = models.CharField(max_length=200)
    quantity = models.IntegerField()







