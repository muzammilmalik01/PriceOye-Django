from rest_framework import viewsets
from orders.models import Order, OrderDetail, Cart
from orders.serializers import OrderSerializer, OrderDetailSerializer, CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Order model.

    This class inherits from ModelViewSet and provides actions for 
    creating, retrieving, updating, and deleting Order instances.

    Attributes:
        queryset: The queryset of Order instances that this view should display.
        serializer_class: The serializer class this view should use to serialize 
                          and deserialize data.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the OrderDetail model.

    This class inherits from ModelViewSet and provides actions for 
    creating, retrieving, updating, and deleting OrderDetail instances.

    Attributes:
        queryset: The queryset of OrderDetail instances that this view should display.
        serializer_class: The serializer class this view should use to serialize 
                          and deserialize data.
    """
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Cart model.

    This class inherits from ModelViewSet and provides actions for 
    creating, retrieving, updating, and deleting Cart instances.

    Attributes:
        queryset: The queryset of Cart instances that this view should display.
        serializer_class: The serializer class this view should use to serialize 
                          and deserialize data.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer