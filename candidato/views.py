from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from candidato.models import Candidato

class candidatoList(ListView):
    model = Candidato

class candidatoCreate(CreateView):
    model = Candidato
    fields = ['nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone']
    success_url = reverse_lazy('usuario:usuario_list')

class candidatoUpdate(UpdateView):
    model = Candidato
    fields = ['nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone']
    success_url = reverse_lazy('usuario:usuario_list')

class candidatoDelete(DeleteView):
    model = Candidato
    success_url = reverse_lazy('usuario:usuario_list')
