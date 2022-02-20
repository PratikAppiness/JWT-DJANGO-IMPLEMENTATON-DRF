from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category','created_on','modefied_on')
    list_per_page = 10


@admin.register(models.Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category','product_title','price','description','created_on','modefied_on')
    list_filter = ("category","created_on")
    list_per_page = 10
    search_fields = ['product_title','category__category']