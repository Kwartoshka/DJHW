from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import DateFromToRangeFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import AdvertisementSerializer
from .models import Advertisement


class IsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        ad_id = request.get_full_path()[20:-1]
        creator = Advertisement.objects.get(id=ad_id).creator
        if user == creator:
            return True


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return IsAdminUser() or IsAuthor()


class Filter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = Filter
    serializer_class = AdvertisementSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAuthorOrAdmin()]
        return []
