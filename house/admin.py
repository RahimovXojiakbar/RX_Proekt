from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.House)
class HouseAdmin(ModelAdmin):
    list_display = ['uuid', 'house_number', 'a_b']
    list_filter = ['neighborhood', 'a_b']
    search_fields = ['house_number']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.HouseStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'house']
    list_filter = ['house']
    search_fields = ['house']



