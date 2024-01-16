from django.contrib import admin
from .models import Brand

admin.site.register(Brand)

# Register your models here.

#Create admin class for the models.
# @admin.register(Brand)
#class CategoryAdmin(admin.ModelAdmin)
    #list_display()
    #search_list()

    #def ProductCount()