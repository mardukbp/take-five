import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from .types import Keyword

@strawberry.type
class Query:
    keywords: list[Keyword] = strawberry_django.field()

schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,  # not required, but highly recommended
    ],
)
