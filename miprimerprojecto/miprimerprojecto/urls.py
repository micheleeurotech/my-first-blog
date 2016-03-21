"""miprimerprojecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^preguntas/$', 'preguntasyrespuestas.views.index', name='preguntas'),
	url(r'^preguntas/(?P<pregunta_id>\d+)/$', 'preguntasyrespuestas.views.pregunta_detalle', name='pregunta_detalle'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^preguntas/crear/$', 'preguntasyrespuestas.views.pregunta_crear', name='pregunta_crear'),
	url(r'^preguntas/editar/(?P<pregunta_id>\d+)/$', 'preguntasyrespuestas.views.pregunta_editar', name='pregunta_editar'),
	url(r'^login/$', 'miprimerprojecto.views.login_page', name='login'),
	url(r'^$', 'miprimerprojecto.views.homepage', name='homepage'),
	url(r'^logout/$', 'miprimerprojecto.views.logout_view', name='logout'),

)

