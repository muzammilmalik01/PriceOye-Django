from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet
from accounts.views import activation

"""
URL patterns for the accounts app.

This module defines the URL patterns for the accounts app in the PriceOye project.
It includes the following patterns:
- Authentication URLs provided by Djoser package.
- Activation URL for account activation.
- API authentication URL for the Django Rest Framework.
- URLs for custom user views provided by the AccountViewSet.

"""

router = DefaultRouter()
router.register(r'customusers',AccountViewSet, basename='customusers')

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('djoser.social.urls')),
    path('activate/<str:uid>/<str:token>/', activation, name='activation'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]