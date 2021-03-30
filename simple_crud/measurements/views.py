from rest_framework.viewsets import ModelViewSet

from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Project.objects.prefetch_related('project').all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.select_related('project').all()
    serializer_class = MeasurementSerializer
