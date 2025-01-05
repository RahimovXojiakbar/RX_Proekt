from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models

@admin.register(models.Governor)
class GovernorAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.District)
class DistrictsAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    list_filter = ['region', 'governor']
    search_fields = ['title']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.DistrictStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'district']
    list_filter = ['district']
    search_fields = ['district']



