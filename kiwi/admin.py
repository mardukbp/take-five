from django.contrib import admin

from kiwi.models import Keyword, KeywordParameter


class Parameters(admin.TabularInline):
    model = KeywordParameter
    extra = 0


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    inlines = [Parameters]
