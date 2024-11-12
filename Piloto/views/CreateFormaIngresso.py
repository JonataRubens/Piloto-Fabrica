from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Piloto.forms.ingressoForm import IngressoForm
from Piloto.models.fomaIngresso import FormaIngresso

class CreateFormaIngresso(CreateView):
    model = FormaIngresso
    
    form_class = IngressoForm
    template_name = 'edit_Aluno/newForma.html'
    success_url = reverse_lazy('lista_alunos')

    def form_valid(self, form):
        aluno = form.save(commit=False)
        aluno.save() 
        return super().form_valid(form)