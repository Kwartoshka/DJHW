from rest_framework.viewsets import ModelViewSet
from .models import Measurement, Project
from .serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # TODO: добавьте конфигурацию для объекта


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    # TODO: добавьте конфигурацию для измерения
