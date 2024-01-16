from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer