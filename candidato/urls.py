from django.conf.urls import patterns, url

from candidato import views

urlpatterns = patterns('',
  url(r'^$', views.candidatoList.as_view(), name='candidato_list'),
  url(r'^new$', views.candidatoCreate.as_view(), name='candidato_new'),
  url(r'^Editar/(?P<pk>\d+)$', views.candidatoUpdate.as_view(), name='candidato_edit'),
  url(r'^Excluir/(?P<pk>\d+)$', views.candidatoDelete.as_view(), name='candidato_delete'),
)
