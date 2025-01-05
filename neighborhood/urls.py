from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('neighborhoods', views.NeighborhoodViewSet, basename='neighborhood')
router.register('statistics', views.StatisticsViewSet, basename='statistic')

urlpatterns = router.urls