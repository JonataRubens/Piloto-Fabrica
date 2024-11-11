from django.contrib import admin
from .models import FormaIngresso
from .models import Aluno, Campus, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeCompleto', 'cpf', 'matricula', 'curso', 'campus', 'situacao', 'formaIngresso',"foto",'dataIngresso')
    search_fields = ('nomeCompleto', 'cpf', 'matricula')
    list_filter = ('campus', 'situacao', 'formaIngresso', )
    readonly_fields = ('matricula',)

    def save_model(self, request, obj, form, change):
        if not obj.matricula:  
            obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Campus)
admin.site.register(Curso)
admin.site.register(FormaIngresso)