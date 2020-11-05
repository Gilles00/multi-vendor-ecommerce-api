from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from vendor.models import Supplier
from customer.models import Customer


# product sub-category
class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    alternativeName = models.CharField(max_length=150)
    description = models.TextField()
    dttm = models.DateTimeField()

    def __str__(self):
        return self.name

# product category
class Category(models.Model):
    category = models.ForeignKey(SubCategory)
    name = models.CharField(max_length=150)
    alternativeName = models.CharField(max_length=150)
    description = models.TextField()
    dttm = models.DateTimeField()
    def __str__(self):
        return self.name




#product Information
class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    supplier = models.ForeignKey(Supplier)
    price = models.IntegerField()
    quantity = models.IntegerField()
    subcategory = models.ForeignKey(SubCategory)
    alternativeNames = models.CharField(max_length=150)
    isActive = models.BooleanField()
    dttm = models.DateTimeField()
    view = models.IntegerField()
    description = models.TextField()
    warranty = models.IntegerField(null=True)
    minimumOrderQuantity = models.IntegerField()
    maximumOrderQuantity = models.IntegerField()

    def __str__(self):
        return self.name



# product Images
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

# product Percest
class Percest(models.Model):
    supplier = models.ForeignKey(Supplier)
    price = models.IntegerField()
    buyingPrice = models.IntegerField()
    date = models.DateField()
    additional = models.CharField(max_length=150)

# Product Review
class Review(models.Model):
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)
    review = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

# discount
class Discount(models.Model):
    product = models.ForeignKey(Product)
    discount = models.CharField(max_length=200)
    discountPercentage = models.IntegerField()
    discountAmount = models.IntegerField()
    discountStatus = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()


# Coupon
class Coupon(models.Model):
    product = models.ForeignKey(Product)
    couponCode = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    discount = models.ForeignKey(Discount)
    limit = models.CharField(max_length=70)


# Warranty
class Warranty(models.Model):
    duration = models.IntegerField()
    policy = models.TextField()

# Custom offer
class Offer(models.Model):
    supplier= models.ForeignKey(Supplier)
    products = models.ForeignKey(Product)
    offerDescription = models.CharField(max_length= 200)





