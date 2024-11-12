from django.urls import path
from Piloto.views import CadastrarAlunoView, CampusCreateView, CreateFormaIngresso, CursoCreateView, CursosPorCampusView, DefaultView, ListaAlunosView


urlpatterns = [
    path('', DefaultView.as_view(), name='index'),
    path('cadastrar/', CadastrarAlunoView.as_view(), name='cadastrar_aluno'),
    path('alunos/', ListaAlunosView.as_view(), name='lista_alunos'),
    path('curso/add/', CursoCreateView.as_view(), name='cadastrarCurso'),
    path('campus/add/', CampusCreateView.as_view(), name='cadastrarCampus'),
    path('cursosCampus/<int:campus_id>/', CursosPorCampusView.as_view(), name='cursosCampus'),
    path('ingresso/', CreateFormaIngresso.as_view(), name='formaDeIngresso'),
]