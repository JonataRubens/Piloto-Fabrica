from django import forms

from Piloto.models import FormaIngresso


class IngressoForm(forms.ModelForm):
    class Meta:
        model = FormaIngresso
        fields = ['nome']