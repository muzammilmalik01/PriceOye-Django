from django.db import models
from accounts.models import CustomUser
from shop.models import Product


class Order(models.Model):
    """
    Model representing an order made by a user.

    Attributes:
        user: The user who made the order.
        order_date: The date and time when the order was made.
        total_amount: The total amount of the order.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        """
        String representation of the Order instance.

        Returns:
            str: A string representing the order, including the user and total amount.
        """
        return f'{self.user} |RS. {self.total_amount}'


class OrderDetail(models.Model):
    """
    Model representing the details of an order.

    Attributes:
        order: The order that the details belong to.
        product: The product that was ordered.
        quantity: The quantity of the product that was ordered.
        subtotal: The subtotal for the product.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        """
        String representation of the OrderDetail instance.

        Returns:
            str: A string representing the order detail, including the order, product, and subtotal.
        """
        return f'Order:{self.order}\nProduct: {self.product}\nSub-Total: {self.subtotal}'


class Cart(models.Model):
    """
    Model representing a shopping cart.

    Attributes:
        user: The user who owns the cart.
        product: The product that is in the cart.
        quantity: The quantity of the product that is in the cart.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()