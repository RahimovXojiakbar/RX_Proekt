from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register('chairmans', views.ChairmanViewSet, basename='chairman')
router.register('MFYs', views.MFYViewSet, basename='MFY')
router.register('statistics', views.StatisticsViewSet, basename='statistics')

urlpatterns = router.urls