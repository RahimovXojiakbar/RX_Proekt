from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('presidents', views.PresidentViewSet, basename='president')
router.register('states', views.StatesViewSet, basename='state')
router.register('statistics', views.StatisticsViewSet, basename='statistics')


urlpatterns = router.urls


