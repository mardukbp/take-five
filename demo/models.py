from django.db import models


class KeywordType(models.TextChoices):
    LIBRARY = 'LIBRARY', 'Library'
    RESOURCE = 'RESOURCE', 'Resource'

class Window(models.Model):
    name = models.CharField(max_length=255)

class Keyword(models.Model):
    type = models.CharField(max_length=255, choices=KeywordType.choices)
    name = models.CharField(max_length=255)
    windows = models.ManyToManyField(Window)

class Parameter(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
