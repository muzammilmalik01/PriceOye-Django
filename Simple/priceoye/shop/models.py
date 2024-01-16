from django.db import models
from brands.models import Brand
from categories.models import Category

class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name: The name of the product.
        description: A description of the product.
        price: The price of the product.
        stock_quantity: The quantity of the product in stock.
        brand: The brand of the product. This can be null if the product 
                does not have a brand.
        category: The category of the product. This can be null if the product 
                   does not have a category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        """
        String representation of the Product instance.

        Returns:
            str: The name of the product.
        """
        return f"{self.name}"    