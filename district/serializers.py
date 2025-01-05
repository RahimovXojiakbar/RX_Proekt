from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class DistrictGovernorSerializer(ModelSerializer):
    class Meta:
        model  = models.Governor
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class DistrictSerializer(ModelSerializer):
    region = SlugRelatedField(slug_field = 'title', read_only=True)
    governor = SlugRelatedField(slug_field = 'name', read_only = True)
    class Meta:
        model = models.District
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class DistrictStatisticsSerializer(ModelSerializer):
    district = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.DistrictStatistics
        fields = '__all__'

        