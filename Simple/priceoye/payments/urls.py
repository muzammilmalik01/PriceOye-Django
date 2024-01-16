from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'Payments', PaymentViewSet, basename='Payments')
router.register(r'Invoice', InvoiceViewSet, basename='Invoice')

urlpatterns = [
    path('', include(router.urls)),
]