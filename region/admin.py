from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.Governor)
class GovernorAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.Region)
class RegionAdmin(ModelAdmin):
    list_display = ['uuid', 'title', 'governor']
    list_filter = ['state', 'governor']
    search_fields = ['title']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.RegionStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'region']
    list_filter = ['region']
    search_fields = ['region']

