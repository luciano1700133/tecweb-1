from django.conf.urls import patterns, url

from aluno import views

urlpatterns = patterns('',
  url(r'^$', views.alunoList.as_view(), name='aluno_list'),
  url(r'^new$', views.alunoCreate.as_view(), name='aluno_new'),
  url(r'^Editar/(?P<pk>\d+)$', views.alunoUpdate.as_view(), name='aluno_edit'),
  url(r'^Excluir/(?P<pk>\d+)$', views.alunoDelete.as_view(), name='aluno_delete'),
)
