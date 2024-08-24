import strawberry_django
from strawberry import auto

from . import models


@strawberry_django.type(models.KeywordParameter)
class KeywordParameter:
    id: auto
    name: auto


@strawberry_django.type(models.Keyword)
class Keyword:
    id: auto
    name: auto
    parameters: list[KeywordParameter]
