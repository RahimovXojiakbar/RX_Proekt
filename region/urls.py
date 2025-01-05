from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('regions', views.RegionViewSet, basename='region')
router.register('governors', views.GovernorViewSet, basename='governor')
router.register('statistics', views.StatisticsViewSet, basename='statistics')


urlpatterns = router.urls

