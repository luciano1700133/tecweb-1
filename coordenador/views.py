from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from coordenador.models import Coordenador

class coordenadorList(ListView):
    model = Coordenador

class coordenadorCreate(CreateView):
    model = Coordenador
    fields = ['nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone']
    success_url = reverse_lazy('coordenador:coordenador_list')

class coordenadorUpdate(UpdateView):
    model = Coordenador
    fields = ['nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone']
    success_url = reverse_lazy('coordenador:coordenador_list')

class coordenadorDelete(DeleteView):
    model = Coordenador
    success_url = reverse_lazy('coordenador:coordenador_list')
