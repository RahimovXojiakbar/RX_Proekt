from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class RegionGovernorSerializer(ModelSerializer):
    class Meta:
        model = models.Governor
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class RegionsSerializer(ModelSerializer):
    state = SlugRelatedField(slug_field = 'title', read_only=True)
    governor = SlugRelatedField(slug_field = 'name', read_only = True)
    class Meta:
        model = models.Region
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class RegionStatisticsSerializer(ModelSerializer):
    state = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.RegionStatistics
        fields = '__all__'



    
