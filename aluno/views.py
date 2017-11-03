from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from aluno.models import Aluno

class alunoList(ListView):
    model = Aluno

class alunoCreate(CreateView):
    model = Aluno
    fields = ['ra', 'nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'curso']
    success_url = reverse_lazy('aluno:aluno_list')

class alunoUpdate(UpdateView):
    model = Aluno
    fields = ['ra', 'nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'curso']
    success_url = reverse_lazy('aluno:aluno_list')

class alunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno:aluno_list')
