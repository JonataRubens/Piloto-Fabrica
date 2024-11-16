from django.contrib import admin
from piloto.models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeCompleto', 'cpf', 'matricula', 'curso','getCampus', 'formaIngresso', 'situacao', 'dataCadastro', 'ativo')
    search_fields = ('nomeCompleto', 'cpf', 'matricula')
    list_filter = ('curso', 'situacao', 'formaIngresso', 'ativo' )
    readonly_fields = ()
    exclude = ('matricula', 'dataCadastro', )

    def getCampus(self, obj):
        return obj.curso.campus.nome  # Ajuste para refletir o relacionamento real
    getCampus.short_description = 'Campus'

    def save_model(self, request, obj, form, change):
        if not obj.matricula:
            obj.save()
        super().save_model(request, obj, form, change)
