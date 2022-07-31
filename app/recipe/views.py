from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from core.models import Tag
from recipe.serializers import TagSerializer


class TagViewSet(ListModelMixin, GenericViewSet):
    """Manage tags in the database"""
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
    
    