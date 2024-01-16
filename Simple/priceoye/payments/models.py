from django.db import models
from accounts.models import CustomUser
from orders.models import Order

class Payment(models.Model):
    """
    Model representing a payment made by a user.

    Attributes:
        user: The user who made the payment.
        amount: The amount of the payment.
        timestamp: The date and time when the payment was made.
        success: A boolean indicating whether the payment was successful.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)


class Invoice(models.Model):
    """
    Model representing an invoice for an order.

    Attributes:
        order: The order that the invoice is for.
        amount: The amount of the invoice.
        payment: The payment associated with the invoice. This can be null 
                 if the invoice has not yet been paid.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.ForeignKey(
        Payment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )