from django.conf.urls import patterns, url
from estacionamientos import views

urlpatterns = patterns('',
                       url(r'^$', views.crearEstacionamiento, name='Nuevo estacionamiento'),
                       url(r'^index/$', views.index, name='index'),
)