from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Piloto.forms.alunoForm import AlunoForm
from Piloto.models import Aluno

class CadastrarAlunoView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'edit_Aluno/new_Aluno.html'
    success_url = reverse_lazy('lista_alunos')