from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField



class HouseSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only=True)
    
    class Meta:
        model = models.House
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class HouseStatisticsSerializer(ModelSerializer):
    house = SlugRelatedField(slug_field = 'house_number', read_only=True)

    class Meta:
        model = models.HouseStatistics
        fields = '__all__'

