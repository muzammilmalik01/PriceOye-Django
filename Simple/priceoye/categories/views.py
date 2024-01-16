from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with Category objects.

    Provides CRUD operations (Create, Retrieve, Update, Delete) for Category objects.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
