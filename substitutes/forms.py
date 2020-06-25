from django import forms


class SearchForm(forms.Form):
    research = forms.CharField(max_length=100)
