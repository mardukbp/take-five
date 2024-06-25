from django.contrib import admin

from apps.keywords.features.keyword.admin import KeywordAdmin
from apps.keywords.features.keyword.models import Keyword


@admin.register(Keyword)
class Admin(KeywordAdmin):
    pass
