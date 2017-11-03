from django.conf.urls import patterns, url

from usuarios_fbv import views

urlpatterns = patterns('',
  url(r'^$', views.usuario_list, name='usuario_list'),
  url(r'^new$', views.usuario_create, name='usuario_new'),
  url(r'^edit/(?P<pk>\d+)$', views.usuario_update, name='usuario_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.usuario_delete, name='usuario_delete'),
)
