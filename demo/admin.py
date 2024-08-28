from django.contrib import admin
from django.db import models

import django_selectize
import django_selectize.forms
from unfold.admin import ModelAdmin, TabularInline

from demo.models import Keyword, Parameter, Window

class Parameters(TabularInline):
    model = Parameter
    tab = True

@admin.register(Keyword)
class KeywordAdmin(ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': django_selectize.forms.SelectizeMultipleWidget
        }
    }
    inlines = [Parameters]

@admin.register(Window)
class WindowAdmin(ModelAdmin):
    pass
