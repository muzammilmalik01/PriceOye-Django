# from django.contrib import admin
# from .models import Product

# admin.site.register(Product)

# # Register your models here.


from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category', 'price']  # Add filters for category and price
    search_fields = ['name']