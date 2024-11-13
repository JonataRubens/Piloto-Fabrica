from django.contrib import admin
from Piloto.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeCompleto', 'cpf', 'matricula', 'curso', 'campus', 'formaIngresso', 'situacao', 'dataCadastro','ativo')
    search_fields = ('nomeCompleto', 'cpf', 'matricula')
    list_filter = ('campus', 'situacao', 'formaIngresso', )
    readonly_fields = ('dataCadastro',)

    exclude = ('campus', 'ativo', 'matricula', )

    def save_model(self, request, obj, form, change):
        if not obj.matricula:  
            obj.save()
        super().save_model(request, obj, form, change)