from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from estacionamientos.forms import EstacionamientosForm


def index(request):
    return render_to_response('estacionamientos/index.html')

def crearEstacionamiento(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = EstacionamientosForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = EstacionamientosForm()
            
    return render_to_response('estacionamientos/crear_estacionamiento.html', {'form': form}, context)