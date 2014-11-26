from django.conf.urls import patterns, url
from estacionamientos import views
from estacionamientos.forms import PagoForm, ReservaForm
from estacionamientos.views import ContactWizard, FORMS

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<id_est>\d+)/$', views.index, name='index'),
                       url(r'^layout/$', views.layout, name='layout'),
                       url(r'^nuevo/$', views.crearEstacionamiento, name='Nuevo estacionamiento'),
                       url(r'^(?P<id_est>\d+)/$', views.verEstacionamiento, name='detalles'),
                       url(r'^(?P<id_est>\d+)/editar/$', views.editarEstacionamiento, name="edicion"),
                       url(r'^reservas/$', views.verReservas, name="lista reservas"),
                       url(r'^pago/$', views.pagarReserva, name="pago"),
                       url(r'^nueva_reserva/$', ContactWizard.as_view(FORMS)),
)