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

    def clean(self):
        cleaned_data = super().clean()
        brand = cleaned_data.get("brand")
        item = cleaned_data.get("item")
        model = cleaned_data.get("model")
        age = cleaned_data.get("age")

        # ここでバリデーション処理を行う
        # バリデーションに失敗した場合は、ValidationErrorを発生させる
        # ValidationErrorはフィールド単位で発生させることも可能

        return cleaned_data
