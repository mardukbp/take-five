from django.contrib import admin

from keywords.features.parameters.admin import ParametersAdmin


class KeywordAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ParametersAdmin]
