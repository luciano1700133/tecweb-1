from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^aluno/', include('aluno.urls', namespace='aluno')),
    url(r'^candidato/', include('candidato.urls', namespace='candidato')),
    url(r'^coordenador/', include('coordenador.urls', namespace='coordenador')),
    url(r'^professor/', include('professor.urls', namespace='professor')),
    url(r'^usuarios_fbv/', include('usuarios_fbv.urls', namespace='usuarios_fbv')),
    url(r'^usuarios_fbv_user/', include('usuarios_fbv_user.urls', namespace='usuarios_fbv_user')),
    url(r'^$', 'apps.views.home'),
]
