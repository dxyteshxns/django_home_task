from django import forms
from flats.models import Flat


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ("owner", )
