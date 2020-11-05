from django.contrib import admin
from .models import SubCategory, Category, Product, ProductImages, Percest, Review, Discount, Coupon, Warranty, Offer
# Register your models here.

@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ['name','alternativeName', 'description', 'dttm']

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name','alternativeName', 'description', 'dttm']

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['code','name','supplier', 'price', 'quantity','subcategory','alternativeNames','isActive','dttm','view','description','warranty','minimumOrderQuantity','maximumOrderQuantity']

@admin.register(ProductImages)
class ProductImages(admin.ModelAdmin):
    list_display = ['product', 'images']


@admin.register(Percest)
class Percest(admin.ModelAdmin):
    list_display = ['supplier','price', 'buyingPrice', 'date','additional']


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['product','customer', 'review', 'status','rating']

@admin.register(Discount)
class Discount(admin.ModelAdmin):
    list_display = ['product','discount', 'discountPercentage', 'discountAmount','discountStatus', 'startDate', 'endDate']

@admin.register(Coupon)
class Coupon(admin.ModelAdmin):
    list_display = ['product','couponCode', 'startDate', 'endDate','discount', 'limit']


@admin.register(Warranty)
class Warranty(admin.ModelAdmin):
    list_display = ['duration', 'policy']


@admin.register(Offer)
class Offer(admin.ModelAdmin):
    list_display = ['supplier', 'products', 'offerDescription']
