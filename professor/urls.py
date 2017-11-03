from django.conf.urls import patterns, url

from professor import views

urlpatterns = patterns('',
  url(r'^$', views.professorList.as_view(), name='professor_list'),
  url(r'^new$', views.professorCreate.as_view(), name='professor_new'),
  url(r'^Editar/(?P<pk>\d+)$', views.professorUpdate.as_view(), name='professor_edit'),
  url(r'^Excluir/(?P<pk>\d+)$', views.professorDelete.as_view(), name='professor_delete'),
)
