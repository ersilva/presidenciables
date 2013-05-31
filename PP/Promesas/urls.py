from django.conf.urls import patterns, url

from Promesas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'perfil/(?P<candidato_id>\d+)', views.perfil, name='perfil')
)