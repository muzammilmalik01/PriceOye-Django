from rest_framework import serializers
from orders.models import OrderDetail, Order, Cart


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer class for the OrderDetail model.

    This class inherits from ModelSerializer and is used to convert 
    OrderDetail instances into JSON format for API responses. It also 
    validates incoming JSON data and converts it back into an OrderDetail 
    instance for database storage.

    Attributes:
        model: The model class that this serializer should use to create 
               instances.
        fields: The fields that should be included in the serialized output.
    """
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Order model.

    This class inherits from ModelSerializer and is used to convert 
    Order instances into JSON format for API responses. It also 
    validates incoming JSON data and converts it back into an Order 
    instance for database storage.

    Attributes:
        model: The model class that this serializer should use to create 
               instances.
        fields: The fields that should be included in the serialized output.
    """
    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Cart model.

    This class inherits from ModelSerializer and is used to convert 
    Cart instances into JSON format for API responses. It also 
    validates incoming JSON data and converts it back into a Cart 
    instance for database storage.

    Attributes:
        model: The model class that this serializer should use to create 
               instances.
        fields: The fields that should be included in the serialized output.
    """
    class Meta:
        model = Cart
        fields = '__all__'
