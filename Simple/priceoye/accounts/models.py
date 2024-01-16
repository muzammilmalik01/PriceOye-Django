from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model for the accounts app.

    Inherits from Django's AbstractUser model and adds an email field.
    The email field is set as the USERNAME_FIELD for authentication.
    """

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','password']

    def __str__(self):
        return self.email

