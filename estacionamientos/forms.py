from django import forms
from estacionamientos.models import Estacionamiento


class EstacionamientosForm(forms.ModelForm):
    
    class Meta:
        model = Estacionamiento
        #fields = ('nombre_duenio', 'nombre_est', 'direccion', 'telefono1', 'telefono2',
        #          'telefono3', 'email1', 'email2', 'email3', 'rif',)
        