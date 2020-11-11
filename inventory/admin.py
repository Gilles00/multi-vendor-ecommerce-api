from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display = ['supplier_name','supplier_phone','supplier_address']


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ['name', 'descriptions']


@admin.register(ProductSubCategory)
class ProductSubCategory(admin.ModelAdmin):
    list_display = ['name','category','descriptions']



@admin.register(ProductWarranty)
class ProductWarranty(admin.ModelAdmin):
    list_display = ['type','limit','conditions']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['code','name','description','category']


@admin.register(ProductImages)
class ProductImages(admin.ModelAdmin):
    list_display = ['product', 'image']


@admin.register(ProductPurchased)
class ProductPurchased(admin.ModelAdmin):
    list_display = ['product', 'supplier','selling_price','buying_price']


@admin.register(ProductReview)
class ProductReview(admin.ModelAdmin):
    list_display = ['product', 'review']


@admin.register(Discount)
class Discount(admin.ModelAdmin):
    list_display = ['product', 'discount_percentage','discount_amount']


@admin.register(Coupon)
class Coupon(admin.ModelAdmin):
    list_display = ['coupon_code', 'start_date','end_date']


@admin.register(CustomOffer)
class CustomOffer(admin.ModelAdmin):
    list_display = ['title', 'product', 'offer_description']



