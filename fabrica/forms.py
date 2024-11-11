# fabrica/forms.py

from django import forms

from .models.fomaIngresso import FormaIngresso
from .models.Campus import Campus
from .models.Curso import Curso
from .models.Aluno import Aluno

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'campus']

    campus = forms.ModelChoiceField(queryset=Campus.objects.all(), empty_label="Selecione o Campus", required=True)

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nomeCompleto', 'cpf', 'curso', 'campus', 
            'dataNascimento', 'foto', 'situacao', 'formaIngresso'
        ]

class IngressoForm(forms.ModelForm):
    class Meta:
        model = FormaIngresso
        fields = ['nome']