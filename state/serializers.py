from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField



class PresidentSerializer(ModelSerializer):
    class Meta:
        model = models.President
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StatesSerializer(ModelSerializer):
    president = SlugRelatedField(slug_field = 'name', read_only = True)
    class Meta:
        model = models.State
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
class StateStatisticsSerializer(ModelSerializer):
    state = SlugRelatedField(slug_field = 'title', read_only = True)
    class Meta:
        model = models.StateStatistics
        fields = '__all__'

