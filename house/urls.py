from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('houses', views.HouseViewSet, basename='house')
router.register('statistics', views.StatisticsView, basename='statistic')


urlpatterns = router.urls