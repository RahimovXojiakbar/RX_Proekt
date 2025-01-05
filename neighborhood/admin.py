from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin

@admin.register(models.Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    list_filter = ['MFY']
    search_fields = ['title']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.NeighborhoodStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'neighborhood']
    list_filter = ['neighborhood']
    search_fields = ['neighborhood']
