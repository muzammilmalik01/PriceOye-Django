from rest_framework import viewsets
from .models import Brand
from .serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on Brand objects.

    Inherits from viewsets.ModelViewSet which provides default
    implementations for the standard list, create, retrieve,
    update, and destroy actions.

    Attributes:
        queryset (QuerySet): The queryset of Brand objects.
        serializer_class (Serializer): The serializer class for Brand objects.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer