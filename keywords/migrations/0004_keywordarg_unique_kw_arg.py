# Generated by Django 4.2.13 on 2024-05-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0003_keyword_doc'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='keywordarg',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_kw_arg'),
        ),
    ]
