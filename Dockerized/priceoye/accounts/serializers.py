from rest_framework.serializers import ModelSerializer
from accounts.models import CustomUser

class AccountSerializer(ModelSerializer):
    """
    Serializer class for the Account model.
    Attributes:
        model: The model class that this serializer should use to create 
               instances.
        fields: The fields that should be included in the serialized output.
    """
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','password']
        # fields = '__all__'