from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from base.serializers import BaseModelSerializer
from base.models import BaseModel

class BaseModelViewSet(ModelViewSet):
    """
    Base viewset for models that extend BaseModel
    """
    serializer_class = BaseModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Override the get_queryset method to filter out soft-deleted objects.
        """
        return self.queryset.filter(deleted_at__isnull=True)

    def perform_destroy(self, instance):
        """
        Override the perform_destroy method to implement soft delete.
        """
        instance.delete(user=self.request.user)