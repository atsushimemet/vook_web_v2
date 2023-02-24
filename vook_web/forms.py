from django import forms
from django.forms import Select

from .choice import CHOICES_AGE, CHOICES_BRAND, CHOICES_ITEM, CHOICES_MODEL


class SearchForm(forms.Form):
    brand = forms.ChoiceField(
        choices=CHOICES_BRAND,
        label="ブランド",
        widget=Select(attrs={"style": "width: 400px"}),
    )
    item = forms.ChoiceField(
        choices=CHOICES_ITEM,
        label="アイテム",
        widget=Select(attrs={"style": "width: 400px"}),
    )
    model = forms.ChoiceField(
        choices=CHOICES_MODEL,
        label="モデル",
        widget=Select(attrs={"style": "width: 400px"}),
    )
    age = forms.ChoiceField(
        choices=CHOICES_AGE,
        label="年代",
        widget=Select(attrs={"style": "width: 400px"}),
    )
