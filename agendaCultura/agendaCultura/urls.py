"""agendaCultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.core.urlresolvers import reverse_lazy
from apps.home import views
from apps.home import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artistas/', views.perfil_list),
    url(r'^actividades/', views.actividad_user),
    url(r'^create/$', views.perfil_create, name='polls_perfil_create'),
    url(r'^home/', include(urls, namespace='home')),
]
