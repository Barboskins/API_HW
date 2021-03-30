from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProjectViewSet, MeasurementViewSet

router = SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'measurements', MeasurementViewSet, basename='measurements')

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
# ]