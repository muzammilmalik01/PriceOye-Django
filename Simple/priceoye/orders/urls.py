from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'Orders', OrderViewSet, basename='Orders')
router.register(r'Order Details', OrderDetailViewSet, basename='Orders Details')

"""
URL Configuration for the orders app.

This module defines the URL patterns for the orders app in the PriceOye project.
It includes the following views:
- OrderViewSet: Handles the CRUD operations for orders.
- OrderDetailViewSet: Handles the CRUD operations for order details.
- CategoryViewSet: Handles the CRUD operations for categories.

The urlpatterns list includes the registered routes for the above views.
"""

urlpatterns = [
    path('', include(router.urls)),
    # Add other app URLs here
]