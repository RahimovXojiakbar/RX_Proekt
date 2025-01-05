from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('humans', views.HumanViewSet, basename='human')
router.register('statistics', views.StatisticsViewSet, basename='statistics')
router.register('profiles', views.ProfileViewSet, basename='profile')


urlpatterns = router.urls