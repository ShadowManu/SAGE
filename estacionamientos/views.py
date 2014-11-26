from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.contrib.formtools.wizard.views import SessionWizardView
import datetime
from estacionamientos.forms import EstacionamientosForm, ReservaForm, PagoForm
from estacionamientos.models import Estacionamiento, Reserva
from decimal import Decimal, ROUND_HALF_UP
import bisect

def layout(request):
    return render_to_response('estacionamientos/layout.html')

def verificarReserva(est, entrada, salida):
    abreEst = est.horaI
    cierraEst = est.horaF
    iniRestr = est.reservaI
    finRestr = est.reservaF
    
    # Hora de apertura del estacionamiento
    if (abreEst is not None) and (abreEst > entrada):
        return False

    # Hora en que cierra el estacionamiento
    if (cierraEst is not None) and (cierraEst < salida):
        return False
    
    # Hora de reserva restringida
    if (iniRestr is not None) and (finRestr is not None) and (entrada < finRestr) and (salida > iniRestr):
        return False
    
    # Consulta de resevas del estacionamiento
    intersecta = Reserva.objects.filter( Q(horaInicio__lt = salida) & Q(horaFin__gt = entrada), 
                                         estacionamiento = est)
    inis = []
    fins = []
    
    # Recorrer el Queryset O(n), insertion Sort O(n)
    for inter in intersecta:
        inicio = (inter.horaInicio.hour * 60) + inter.horaInicio.minute
        fin    = (inter.horaFin.hour * 60)    + inter.horaFin.minute
        bisect.insort(inis, inicio)
        bisect.insort(fins, fin)
    
    i = 0
    j = 0
    cnt = 0
    # Algoritmo de Marzullo para intervalos O(n) con algunas modificaciones
    while i < len(inis) and j < len(fins):
        if inis[i] < fins [j]:
            cnt = cnt + 1
            i = i + 1
        elif inis[i] == fins[j]:
            i = i + 1
            j = j + 1
        else:
            cnt = cnt - 1
            j = j + 1
        if cnt == est.capacidad:
            return False
    return True
    
def calcularMonto(tarifa, inicio, fin):
    
    diferenciaHoras= fin.hour - inicio.hour
    diferenciaMinutos = fin.minute - inicio.minute
    
    if (diferenciaMinutos == 0):
        return Decimal(tarifa * diferenciaHoras).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    elif (diferenciaMinutos < 0):
        return Decimal(tarifa * diferenciaHoras).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    else:
        return Decimal(tarifa * (1+diferenciaHoras)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        

def crearReserva(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            est = form.cleaned_data['estacionamiento']
            inicio = form.cleaned_data['horaInicio']
            fin = form.cleaned_data['horaFin']
            hayReserva = verificarReserva(est, inicio, fin)
            if hayReserva:
                form.save(commit=True)
            else:
                ocupado = True
                return render_to_response('estacionamientos/crear_reserva.html',
                                          {'form': form, 'ocupado': ocupado, 'estacionamiento': est},
                                          context)                
            return index(request)
    else:
        form = ReservaForm()
    return render_to_response('estacionamientos/crear_reserva.html',
                              {'form': form}, context)

def verDatosPago(request):
    context = RequestContext(request)
    return render_to_response('estacionamientos/verificarReserva.html', {}, context)

# Contact Wizard
FORMS = [("0", ReservaForm),
         ("1", PagoForm),
         ]

TEMPLATES = {"0": "estacionamientos/crear_reserva.html",
             "1": "estacionamientos/pago.html"
             }

class ContactWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_initial(self, step):
        current = self.steps.current
        
        if current == '0':
            formulario = self.storage.get_step_data('0')
            if formulario:
                est_id = formulario.get('0-estacionamiento')
                inicio = datetime.datetime.strptime(formulario.get('0-horaInicio'), "%I:%M %p").time()
                fin = datetime.datetime.strptime(formulario.get('0-horaFin'), "%I:%M %p").time()
                est = Estacionamiento.objects.get(pk=est_id)
                tarifa = est.tarifa
                hayReserva = verificarReserva(est, inicio, fin)
                if hayReserva: 
                    monto = calcularMonto(tarifa, inicio, fin)
                    print (monto)
                    return self.initial_dict.get(step, {'pago': monto})

        return self.initial_dict.get(step, {})

    
    def done(self, form_list, form_dict, **kwargs):      
        form_dict['0'].save()
        form_dict['1'].save()
        return render_to_response('estacionamientos/recibo.html', {'form_data': [form.cleaned_data for form in form_list]})


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
            form.save(commit=True)
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
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        form = PagoForm()
        
    return render_to_response('estacionamientos/pago.html', {'form': form}, context)    

