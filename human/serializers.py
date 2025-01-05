from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField



class HumanSerializer(ModelSerializer):
    house = SlugRelatedField(slug_field = 'house_number', read_only=True)
    
    class Meta:
        model = models.Human
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class HumanStatisticsSerializer(ModelSerializer):
    human = SlugRelatedField(slug_field = 'name', read_only=True)

    class Meta:
        model = models.HumanStatistics
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProfileSerializer(ModelSerializer):
    user =  SlugRelatedField(slug_field = 'username', read_only=True)

    class Meta:
        model = models.Profile
        fields = '__all__'

