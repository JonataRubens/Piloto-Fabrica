from django.urls import reverse_lazy
from Piloto.forms.campusForm import CampusForm
from Piloto.models import Curso
from django.views.generic.edit import CreateView


class CampusCreateView(CreateView):
    model = Curso
    form_class = CampusForm
    template_name = 'edit_Aluno/newCampus.html'
    success_url = reverse_lazy('lista_alunos')