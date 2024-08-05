from django import forms
from .models import Team


class DynamicSelect(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        widget=forms.Select(
            attrs={
                'data-tags': 'true',
                'data-placeholder': 'Select a team'
            }
        )
        super().__init__(*args, widget=widget, **kwargs)

    def to_python(self, value: str):
        if value.isnumeric():
            return super().to_python(value)

        team = Team.objects.create(name=value)
        return super().to_python(team.pk)


class PlayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['team'] = DynamicSelect(
            queryset=Team.objects.all()
        )
