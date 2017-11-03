from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from professor.models import professor

class professorList(ListView):
    model = professor

class professorCreate(CreateView):
    model = professor
    fields = ['nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'materia']
    success_url = reverse_lazy('professor:professor_list')

class professorUpdate(UpdateView):
    model = professor
    fields = ['nome', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'materia']
    success_url = reverse_lazy('professor:professor_list')

class professorDelete(DeleteView):
    model = professor
    success_url = reverse_lazy('professor:professor_list')
