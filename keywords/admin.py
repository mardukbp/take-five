from django.contrib import admin

from keywords.features.keyword.admin import KeywordAdmin
from keywords.features.keyword.models import Keyword


@admin.register(Keyword)
class Admin(KeywordAdmin):
    pass
