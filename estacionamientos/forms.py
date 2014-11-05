from django import forms
from estacionamientos.models import Estacionamiento


class EstacionamientosForm(forms.ModelForm):
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    email2 = forms.EmailField(required=False)
    email3 = forms.EmailField(required=False)
    horaI = forms.TimeField(required=False)
    horaF = forms.TimeField(required=False)
    reservaI = forms.TimeField(required=False)
    reservaF = forms.TimeField(required=False)
    
    
    
    class Meta:
        model = Estacionamiento
        #fields = ('nombre_duenio', 'nombre_est', 'direccion', 'telefono1', 'telefono2',
        #          'telefono3', 'email1', 'email2', 'email3', 'rif',)
        