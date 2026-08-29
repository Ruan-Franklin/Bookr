"""
Base serializer for models that extend BaseModel
"""

from rest_framework.serializers import ModelSerializer
from back.base.models import BaseModel

class BaseModelSerializer(ModelSerializer):
    """
    Base serializer for models that extend BaseModel
    """
    class Meta:
        model = BaseModel
        fields = ["id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        """
        Override the create method to set the created_by and updated_by fields
        based on the user making the request.
        """
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["created_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Override the update method to set the updated_by field based on the user making the request.
        """
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["updated_by"] = request.user
        return super().update(instance, validated_data)