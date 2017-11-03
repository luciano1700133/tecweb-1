from django.conf.urls import patterns, url

from coordenador import views

urlpatterns = patterns('',
  url(r'^$', views.coordenadorList.as_view(), name='coordenador_list'),
  url(r'^new$', views.coordenadorCreate.as_view(), name='coordenador_new'),
  url(r'^Editar/(?P<pk>\d+)$', views.coordenadorUpdate.as_view(), name='coordenador_edit'),
  url(r'^Excluir/(?P<pk>\d+)$', views.coordenadorDelete.as_view(), name='coordenador_delete'),
)
