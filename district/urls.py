from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register('governors', views.GovernorViewSet, basename='governor')
router.register('districts', views.DistrictViewSet, basename='districts')
router.register('statistics', views.StatisticsViewSet, basename='statistics')

urlpatterns = router.urls