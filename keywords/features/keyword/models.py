from typing import TYPE_CHECKING

from django.db.models import Model, CharField, TextField

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager # type: ignore

from keywords.features.parameters.models import KeywordArg


class Keyword(Model):
    name: CharField = CharField(max_length=255)
    doc: TextField = TextField(verbose_name='Documentation', blank=True)

    if TYPE_CHECKING:
        args: RelatedManager["KeywordArg"]

    def __str__(self) -> str:
        return self.name
