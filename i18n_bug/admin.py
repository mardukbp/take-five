from django.contrib import admin
from django import forms

from django_select2.forms import Select2Widget

from i18n_bug.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        widgets = {
            'title': Select2Widget
        }


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
