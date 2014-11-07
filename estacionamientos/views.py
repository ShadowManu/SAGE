from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from estacionamientos.forms import EstacionamientosForm
from models import Estacionamiento


def index(request):
    context = RequestContext(request)
    listaEst = Estacionamiento.objects.all()
    return render_to_response('estacionamientos/index.html', {'lista': listaEst}, context)

def crearEstacionamiento(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = EstacionamientosForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        form = EstacionamientosForm()
            
    return render_to_response('estacionamientos/crear_estacionamiento.html', {'form': form}, context)

def verEstacionamiento(request, id_est):
    context = RequestContext(request)
    parametros = get_object_or_404(Estacionamiento, pk=id_est)
    return render_to_response('estacionamientos/estacionamiento.html', {'parametros': parametros}, context)