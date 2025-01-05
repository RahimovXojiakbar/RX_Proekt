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

class PresidentViewSet(ModelViewSet):
    queryset = models.President.objects.all()
    serializer_class = serializers.PresidentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['information']
    search_fields = ['name']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StatesViewSet(ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StatesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['president']
    search_fields = ['title']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StatisticsViewSet(ModelViewSet):
    queryset = models.StateStatistics.objects.all()
    serializer_class = serializers.StateStatisticsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['state']
    search_fields = ['state']
    pagination_class = MyPagination

