from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from estacionamientos.forms import EstacionamientosForm, ReservaForm, PagoForm
from estacionamientos.models import Estacionamiento, Reserva, Puesto
from decimal import Decimal, ROUND_HALF_UP
import bisect

def layout(request):
    RequestContext(request)
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
    
def calcularMonto(reserva):
    tarifa = reserva.estacionamiento.tarifa
    inicio = reserva.horaInicio
    fin = reserva.horaFin
    
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
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        form = PagoForm()
            
    return render_to_response('estacionamientos/pago.html', {'form': form}, context)    

