from django.db import models

class Brand(models.Model):
    """
    Represents a brand in the system.

    Attributes:
        name (str): The name of the brand.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name