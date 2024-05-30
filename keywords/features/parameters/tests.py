from django.test import TestCase
from django.db.utils import IntegrityError

from keywords.features.keyword.models import Keyword
from keywords.features.parameters.models import KeywordArg


class ParametersTests(TestCase):
    def test_unique_parameter_name(self):
        kw = Keyword.objects.create(name='Test Keyword')
        KeywordArg.objects.create(
            keyword=kw,
            name='arg1',
            default_value='val1'
        )

        with self.assertRaisesMessage(
            IntegrityError, 
            expected_message='UNIQUE constraint failed: keywords_keywordarg.name'
            ):
            
            KeywordArg.objects.create(
                keyword=kw,
                name='arg1',
                default_value='val1'
            )
