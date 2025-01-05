from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField



class NeighborhoodSerializer(ModelSerializer):
    MFY = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.Neighborhood
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class NeighborhoodStatisticsSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only=True)
    
    class Meta:
        model = models.NeighborhoodStatistics
        fields = '__all__'

        