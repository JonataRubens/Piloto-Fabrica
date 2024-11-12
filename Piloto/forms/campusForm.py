from django import forms
from Piloto.models import Campus


class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']