from rest_framework.serializers import ModelSerializer
from brands.models import Brand


class BrandSerializer(ModelSerializer):
    """
    Serializer class for the Brand model.
    """

    class Meta:
        model = Brand
        fields = '__all__'