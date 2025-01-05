from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin


@admin.register(models.Chairman)
class ChairmanAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    list_filter = ['information']
    search_fields = ['name']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.MFY)
class MFYAdmin(ModelAdmin):
    list_display = ['uuid', 'title', 'district']
    list_filter = ['chairman', 'district']
    search_fields = ['title']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.MFYStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'MFY']
    list_filter = ['MFY']
    search_fields = ['MFY']


