from django.http import JsonResponse
from django.views import View
from Piloto.models import Curso


class CursosPorCampusView(View):
    def get(self, request, campus_id):
        cursos = Curso.objects.filter(campus_id=campus_id).values('id', 'nome')
        return JsonResponse({'cursos': list(cursos)})