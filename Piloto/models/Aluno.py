from datetime import date
from django.db import models
from .Situacao import Situacao
from .fomaIngresso import FormaIngresso
from .Curso import Curso

class Aluno(models.Model):
    nomeCompleto = models.CharField('Nome completo', max_length=500, help_text='')
    cpf = models.CharField('CPF', max_length=11, unique=True, help_text='')
    matricula = models.CharField('Matricula', max_length=10, unique=True, editable=False)
    curso = models.ForeignKey(Curso, verbose_name="Curso", on_delete=models.PROTECT)
    dataNascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField("foto Aluno", upload_to='alunos_fotos/', blank=True, null=True)

    situacao = models.ForeignKey(Situacao, verbose_name="Situação", on_delete=models.PROTECT)

    formaIngresso = models.ForeignKey(FormaIngresso, verbose_name="Forma de Ingresso", on_delete=models.PROTECT)
    dataCadastro = models.DateField('data de cadastro', default=date.today, blank=True, null=True)
    dataUpdate = models.DateTimeField('Ultima atualização', auto_now=True)  
    ativo = models.BooleanField("Aluno vinculado na instituição?", default=True)

    def __str__(self):
        return f"{self.nomeCompleto} ({self.matricula})"
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def save(self, *args, **kwargs):
        if not self.pk and not self.matricula:
            self.matricula = self.GerarMatricula()
        if self.curso and self.curso.campus:
            self.campus = self.curso.campus
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Lógica de matrícula
        if not self.matricula:
            self.matricula = self.GerarMatricula()
        super().save(*args, **kwargs)

    def GerarMatricula(self):
        ano = self.dataCadastro.strftime('%Y') 
        semestre = '1' if self.dataCadastro.month <= 6 else '2'
        ultima_matricula = Aluno.objects.filter(matricula__startswith=f'{ano}{semestre}').order_by('-matricula').first()
        sequencia = int(ultima_matricula.matricula[-4:]) + 1 if ultima_matricula else 1
        return f'{ano}{semestre}{str(sequencia).zfill(4)}'
