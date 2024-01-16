from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Product model.
    """
    class Meta:
        model = Product
        fields = '__all__'
