from django import forms
from flats.models import Flat, DealRequest


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ("owner", )


class DealRequestForm(forms.ModelForm):
    class Meta:
        model = DealRequest
        exclude = ("seeker", "flat", "status", "date_approved")