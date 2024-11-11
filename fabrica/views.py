from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models.fomaIngresso import FormaIngresso
from fabrica.forms import  CursoForm, AlunoForm, CampusForm, IngressoForm
from fabrica.models import Aluno, Campus, Curso
from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView
from .models import SITUACAO_CHOICES 

class DefaultView(TemplateView):
    template_name = 'index.html'

class CadastrarAlunoView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'edit_Aluno/new_Aluno.html'
    success_url = reverse_lazy('lista_alunos')

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
        context['SITUACAO_CHOICES'] = SITUACAO_CHOICES
        return context

class CursosPorCampusView(View):
    def get(self, request, campus_id):
        cursos = Curso.objects.filter(campus_id=campus_id).values('id', 'nome')
        return JsonResponse({'cursos': list(cursos)})

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'edit_Aluno/newCurso.html'
    success_url = reverse_lazy('lista_alunos')

class CampusCreateView(CreateView):
    model = Curso
    form_class = CampusForm
    template_name = 'edit_Aluno/newCampus.html'
    success_url = reverse_lazy('lista_alunos')

class CreateFormaIngresso(CreateView):
    model = FormaIngresso
    
    form_class = IngressoForm
    template_name = 'edit_Aluno/newForma.html'
    success_url = reverse_lazy('lista_alunos')

    def form_valid(self, form):
        aluno = form.save(commit=False)
        aluno.save() 
        return super().form_valid(form)

#######################TEST#############
