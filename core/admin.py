from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qty', 'slug', 'created_at', 'updated_at', 'active')

