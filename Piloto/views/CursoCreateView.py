from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Piloto.forms.cursoForm import CursoForm
from Piloto.models import Curso

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'edit_Aluno/newCurso.html'
    success_url = reverse_lazy('lista_alunos')