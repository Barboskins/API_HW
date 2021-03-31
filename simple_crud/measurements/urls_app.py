from django.urls import path, include
from rest_framework.routers import  DefaultRouter

from .views import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('measurements', MeasurementViewSet)

urlpatterns = router.urls



