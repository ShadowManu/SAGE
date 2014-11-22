from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.db.models import Q, F
from django.contrib.formtools.wizard.views import SessionWizardView
from estacionamientos.forms import EstacionamientosForm, ReservaForm, PagoForm
from estacionamientos.models import Estacionamiento, Reserva, Puesto


def layout(request):
    return render_to_response('estacionamientos/layout.html')


def verificarReserva(inicio, fin, nombre):
    est = Estacionamiento.objects.get(nombre_est=nombre)
    sinReserva = Puesto.objects.filter(~Q(reserva__puesto=F('id')), estacionamiento=est)
    print "______"
    print sinReserva
    
    if sinReserva:
        return sinReserva[0]
        
    libres = Puesto.objects.filter((Q(reserva__horaInicio__lt=inicio) & Q(reserva__horaFin__lte=inicio) &
                                    Q(reserva__horaInicio__lt=fin) & Q(reserva__horaFin__lt=fin)) |
                                   (Q(reserva__horaInicio__gt=inicio)& Q(reserva__horaFin__gt=inicio) &
                                    Q(reserva__horaInicio__gte=fin) & Q(reserva__horaFin__gt=fin)),
                                   estacionamiento=est)
    
    #libres = Puesto.objects.filter((Q(reserva__horaInicio__gte=fin) & Q(reserva__horaFin__gt=fin) & Q(reserva__horaInicio__gt=inicio) & Q(reserva__horaFin__gt=inicio)) |(Q(reserva__horaInicio__lt=inicio) & Q(reserva__horaFin__lte=inicio) &Q(reserva__horaInicio__lt=fin) & Q(reserva__horaFin__lt=fin)),estacionamiento=est)
    
    reservas = Reserva.objects.filter(puesto__estacionamiento=est)
    print reservas
    
    print libres
    if libres:
        return libres[0]
    else:
        return None
        
        
def crearReserva(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['estacionamiento']
            inicio = form.cleaned_data['horaInicio']
            fin = form.cleaned_data['horaFin']
            puesto = verificarReserva(inicio, fin, nombre)
            if puesto:
                reserva = form.save(commit=False)
                reserva.puesto = puesto
                reserva.save()
            else:
                ocupado = True
                return render_to_response('estacionamientos/crear_reserva.html',
                                          {'form': form, 'ocupado': ocupado, 'estacionamiento': nombre},
                                          context)  
            return index(request)
    else:
        form = ReservaForm()
    return render_to_response('estacionamientos/crear_reserva.html',
                              {'form': form}, context)


class ContactWizard(SessionWizardView):
    template_name = 'estacionamientos/reservas.html'
    
    def done(self, form_list, **kwargs):
        form_data = procesar_form_data(form_list)
        
        return render_to_response('estacionamientos/recibo.html', {'form_data': form_data})


def procesar_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    
    return form_data


def verReservas(request):
    context = RequestContext(request)
    reservas = Reserva.objects.all()
    return render_to_response('estacionamientos/reservas.html',
                              {'reservas': reservas}, context)
    

def index(request, id_est=None):
    context = RequestContext(request)
    listaEst = Estacionamiento.objects.all()
    try:
        parametros = Estacionamiento.objects.get(pk=id_est)
    except Estacionamiento.DoesNotExist:
        parametros = None
    return render_to_response('estacionamientos/index.html',
                              {'lista': listaEst, 'parametros': parametros}, context)


def crearEstacionamiento(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = EstacionamientosForm(request.POST)
        if form.is_valid():
            cap = form.cleaned_data['capacidad']
            est = form.cleaned_data['nombre_est']
            form.save(commit=True)
            i = 1
            aux = Estacionamiento.objects.get(nombre_est=est)
            while (i<=cap):
                Puesto.objects.create(estacionamiento=aux, numero=i)
                i += 1
            return index(request)
    else:
        form = EstacionamientosForm()
            
    return render_to_response('estacionamientos/crear_estacionamiento.html',
                              {'form': form}, context)


def verEstacionamiento(request, id_est):
    context = RequestContext(request)
    parametros = get_object_or_404(Estacionamiento, pk=id_est)
    return render_to_response('estacionamientos/estacionamiento.html',
                              {'parametros': parametros}, context)


def editarEstacionamiento(request, id_est):
    context = RequestContext(request)
    est = get_object_or_404(Estacionamiento, pk=id_est)
    listaEst = Estacionamiento.objects.all()
    if request.method == 'POST':
        form = EstacionamientosForm(request.POST,instance=est)
        if form.is_valid():
            form.save(commit=True)
            return index(request, id_est)
    else:
        form = EstacionamientosForm(instance=est)
    return render_to_response('estacionamientos/editar_estacionamiento.html',
                              {'form': form, 'lista': listaEst}, context)
    

def pagarReserva(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = PagoForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            print "HUEHUEHUE"
            form.save(commit=True)
            return index(request)
    else:
        form = PagoForm()
        
    return render_to_response('estacionamientos/pago.html', {'form': form}, context)    

