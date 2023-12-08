from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_created']
