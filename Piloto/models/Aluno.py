from datetime import date
from django.db import models
from .Situacao import Situacao
from .fomaIngresso import FormaIngresso
from .Curso import Curso
from .Campus import Campus

SITUACAO_CHOICES = [
    (1, 'Vinculado'),
    (2, 'Formado'),
    (3, 'Jubilado'),
    (4, 'Evadido'),
]
class Aluno(models.Model):
    nomeCompleto = models.CharField('Nome completo',max_length=500,help_text='')
    cpf = models.CharField('CPF',max_length=11, unique=True, help_text='')
    matricula = models.CharField('Matricula', max_length=10, unique=True, editable=False)
    curso = models.ForeignKey(Curso, verbose_name="Curso", on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, verbose_name="Campus", on_delete=models.PROTECT)
    dataNascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='alunos_fotos/', blank=True, null=True)
    situacao = models.ForeignKey(Situacao, verbose_name="Situação", on_delete=models.PROTECT)
    formaIngresso = models.ForeignKey(FormaIngresso, verbose_name="Forma de Ingresso", on_delete=models.PROTECT)
    dataIngresso = models.DateField('data de cadastro',default=date.today, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = self.GerarMatricula()
        super().save(*args, **kwargs)

    def GerarMatricula(self):
        ano = self.dataIngresso.strftime('%Y')  # Certifique-se de que 'dataIngresso' é o nome correto
        semestre = '1' if self.dataIngresso.month <= 6 else '2'
        
        # Obter a última matrícula gerada para o ano e semestre
        ultima_matricula = Aluno.objects.filter(matricula__startswith=f'{ano}{semestre}').order_by('-matricula').first()
        
        if ultima_matricula:
            # A sequência vai ser o número extraído da matrícula anterior + 1
            sequencia = int(ultima_matricula.matricula[-4:]) + 1
        else:
            # Caso não haja matrícula anterior, inicia com 1
            sequencia = 1

        return f'{ano}{semestre}{str(sequencia).zfill(4)}'
    
    def __str__(self):
        return f"{self.nomeCompleto} ({self.matricula})"