from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')

"""
URL patterns for the brands app.

This module defines the URL patterns for the brands app in the PriceOye project.
It includes the default router for handling CRUD operations on the 'brands' endpoint.
Other app URLs can be added below the router.urls.

Example usage:
    urlpatterns = [
        path('', include(router.urls)),
        # Add other app URLs here
    ]
"""

urlpatterns = [
    path('', include(router.urls)),
    # Add other app URLs here
]