import uuid

from django.db import models


class KeywordParameter(models.Model):
    keyword = models.ForeignKey(
        'Keyword',
          on_delete=models.CASCADE,
          related_name='parameters'
    )
    name = models.CharField(max_length=255)


class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
