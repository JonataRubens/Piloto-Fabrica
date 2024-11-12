from django import forms
from Piloto.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nomeCompleto', 'cpf', 'curso', 'campus', 
            'dataNascimento', 'foto', 'situacao', 'formaIngresso'
        ]