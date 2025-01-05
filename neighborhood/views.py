from django.shortcuts import render
from . import models , serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class NeighborhoodViewSet(ModelViewSet):
    queryset = models.Neighborhood.objects.all()
    serializer_class = serializers.NeighborhoodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['MFY']
    search_fields = ['title']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StatisticsViewSet(ModelViewSet):
    queryset = models.NeighborhoodStatistics.objects.all()
    serializer_class = serializers.NeighborhoodStatisticsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['neighborhood']
    search_fields = ['neighborhood']
    pagination_class = MyPagination






