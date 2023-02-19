from django import forms


class SearchForm(forms.Form):
    brand = forms.CharField(label="ブランド", max_length=100)
    item = forms.CharField(label="アイテム", max_length=100)
    model = forms.CharField(label="モデル名", max_length=100)
    age = forms.CharField(label="年代", max_length=100)
