from django.db import models

class Category(models.Model):
    """
    Represents a category in the system.

    Attributes:
        name (str): The name of the category.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
