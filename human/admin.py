from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.Human)
class HumanAdmin(ModelAdmin):
    list_display = ['uuid', 'name', 'house__house_number']
    list_filter = ['house', 'status', 'information']
    search_fields = ['name', 'user']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.HumanStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'human']
    list_filter = ['human']
    search_fields = ['human']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['uuid', 'user__username']
    list_filter = ['user__username']
    search_fields = ['user__username']


    