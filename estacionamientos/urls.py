from django.conf.urls import patterns, url
from estacionamientos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^nuevo/$', views.crearEstacionamiento, name='Nuevo estacionamiento'),
                       url(r'^(?P<id_est>\d+)/$', views.verEstacionamiento, name='detalles'),
)