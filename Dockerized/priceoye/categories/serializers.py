from rest_framework.serializers import ModelSerializer
from categories.models import Category


class CategorySerializer(ModelSerializer):
    """
    Serializer class for Category model.
    """

    class Meta:
        model = Category
        fields = '__all__'
