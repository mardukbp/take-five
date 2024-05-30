from django.db import models
from django.db.models import Model, CharField, ForeignKey


class KeywordArg(Model):
    keyword: ForeignKey = ForeignKey('Keyword', related_name='args', on_delete=models.CASCADE)
    name: CharField = CharField(max_length=255)
    default_value: CharField = CharField(max_length=255)

    class Meta:
        verbose_name = 'Parameter'
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_kw_arg')]
