#urls de app home
from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'eventos/$', actividad_list, name='eventos'),
    url(r'artistas/$', perfil_list, name='artistas'),
    url(r'registro/$', perfil_create, name='crear_perfil'),
    url(r'(?P<username>[-\w]+)/crearEvento/$', actividad_create, name='crear_evento'),
    url(r'(?P<username>[-\w]+)/eventos/$', actividad_user, name='actividad_user'),
    url(r'(?P<username>[-\w]+)/editar/$', perfil_edit, name='editar_perfil'),
    url(r'(?P<username>[-\w]+)/$', perfil, name='perfil'),
]
