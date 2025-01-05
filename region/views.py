from django.shortcuts import render
from . import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GovernorViewSet(ModelViewSet):
    queryset = models.Governor.objects.all()
    serializer_class = serializers.RegionGovernorSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter]
    filterset_fields = ['information']
    search_fields = ['name']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class RegionViewSet(ModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['state', 'governor']
    search_fields = ['title']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StatisticsViewSet(ModelViewSet):
    queryset = models.RegionStatistics.objects.all()
    serializer_class = serializers.RegionStatisticsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['region']
    search_fields = ['region']
    pagination_class = MyPagination
    
