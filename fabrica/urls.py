from django.contrib import admin
from django.urls import path
from django.conf import settings
from fabrica.views import CursoCreateView, CampusCreateView
from .views import CadastrarAlunoView, CreateFormaIngresso, CursosPorCampusView, DefaultView, ListaAlunosView
from fabrica import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DefaultView.as_view(), name='index'),
    path('cadastrar/', CadastrarAlunoView.as_view(), name='cadastrar_aluno'),
    path('alunos/', ListaAlunosView.as_view(), name='lista_alunos'),
    path('curso/add/', CursoCreateView.as_view(), name='cadastrarCurso'),
    path('campus/add/', CampusCreateView.as_view(), name='cadastrarCampus'),
    path('cursosCampus/<int:campus_id>/', CursosPorCampusView.as_view(), name='cursosCampus'),
    path('ingresso/', CreateFormaIngresso.as_view(), name='formaDeIngresso'),

   ##################TEST##########################


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)