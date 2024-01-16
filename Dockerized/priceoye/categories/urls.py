from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='Categories')

"""
URL configuration for the categories app.

This module defines the URL patterns for the categories app. It includes the
router URLs for the CategoryViewSet, which handles the CRUD operations for
categories.

Example:
    To access the list of categories, use the following URL:
    - /categories/

    To access a specific category, use the following URL:
    - /categories/{category_id}/

    To create a new category, use the following URL:
    - /categories/create/

    To update an existing category, use the following URL:
    - /categories/{category_id}/update/

    To delete a category, use the following URL:
    - /categories/{category_id}/delete/
"""

urlpatterns = [
    path('', include(router.urls)),
    # Add other app URLs here
]