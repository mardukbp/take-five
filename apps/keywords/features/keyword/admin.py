from django.contrib import admin

from apps.keywords.features.parameters.admin import ParametersAdmin


class KeywordAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ParametersAdmin]
