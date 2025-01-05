from django.shortcuts import render
from . import models,serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ChairmanViewSet(ModelViewSet):
    queryset = models.Chairman.objects.all()
    serializer_class = serializers.ChairmanSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['information']
    search_fields = ['name']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFYViewSet(ModelViewSet):
    queryset = models.MFY.objects.all()
    serializer_class = serializers.MFYSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['chairman', 'district']
    search_fields = ['title']
    pagination_class = MyPagination

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StatisticsViewSet(ModelViewSet):
    queryset = models.MFYStatistics.objects.all()
    serializer_class = serializers.MFYStatisticsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['MFY']
    search_fields = ['MFY']
    pagination_class = MyPagination


