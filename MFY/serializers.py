from . import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class ChairmanSerializer(ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFYSerializer(ModelSerializer):
    chairman = SlugRelatedField(slug_field = 'name', read_only=True)
    district = SlugRelatedField(slug_field = 'title', read_only=True)
    
    class Meta:
        model = models.MFY
        fields = '__all__'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFYStatisticsSerializer(ModelSerializer):
    MFY = SlugRelatedField(slug_field = 'title', read_only=True)
    
    class Meta:
        ref_name = 'MFYStatisticsSerializer'
        model = models.MFYStatistics
        fields = '__all__'

