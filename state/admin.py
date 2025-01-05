from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models



@admin.register(models.State)
class StateAdmin(ModelAdmin):
    list_display = ['uuid', 'title', 'president']
    search_fields = ['title']
    list_filter = ['president']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.President)
class PresidentAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']
    list_filter = ['information']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(models.StateStatistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['uuid', 'state']
    search_fields = ['state']

