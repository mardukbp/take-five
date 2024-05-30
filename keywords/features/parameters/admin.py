from django.contrib import admin

from keywords.features.parameters.models import KeywordArg


class ParametersAdmin(admin.TabularInline):
    model = KeywordArg
    verbose_name_plural = 'Parameters'
    extra = 0
