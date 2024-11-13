from django.views.generic import ListView
from Piloto.models import Aluno, Campus, Curso
from Piloto.models.fomaIngresso import FormaIngresso
# from Piloto.models import SITUACAO_CHOICES 




class ListaAlunosView(ListView):
    model = Aluno
    template_name = 'listas/listar_Alunos.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        queryset = Aluno.objects.all()
        campus_filter = self.request.GET.get('campus')
        curso_filter = self.request.GET.get('curso')

        if campus_filter:
            queryset = queryset.filter(campus__id=campus_filter)
        if curso_filter:
            queryset = queryset.filter(curso__id=curso_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campus_options'] = Campus.objects.all()
        context['curso_options'] = Curso.objects.all()
        context['formas_ingresso'] = FormaIngresso.objects.all()
        return context