from django import forms
from Piloto.models import Situacao


class IngressoForm(forms.ModelForm):
    class Meta:
        model = Situacao
        fields = ['nome']