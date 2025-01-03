from django.contrib import admin
from django.db import models

from django_select2.forms import Select2AdminMixin, ModelSelect2Widget

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin, Select2AdminMixin):
    formfield_overrides = {
        models.ForeignKey: {
            'widget': ModelSelect2Widget
        }
    }
