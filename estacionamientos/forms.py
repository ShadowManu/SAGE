#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django import forms
from estacionamientos.models import Estacionamiento, Reserva, Pago


class EstacionamientosForm(forms.ModelForm):
    nombre_duenio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Nombre del Dueño',}))
    nombre_est = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Nombre del Estacionamiento',}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Dirección',}))
    telefono1 = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Teléfono 1',}))
    telefono2 = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Telefono 2',}), 
                                   required=False)
    telefono3 = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Teléfono 3',}), 
                                   required=False)
    email1 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Correo Electrónico 1',}))
    email2 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Correo Electrónico 2',}),
                              required=False)
    email3 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Correo Electrónico 3',}),
                              required=False)
    rif = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'RIF',}))
    capacidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Capacidad',}))
    tarifa = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Tarifa',}))
    horaI = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Hora Apertura',}),
                            required=False)
    horaF = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Hora Cierre',}),
                            required=False)
    reservaI = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Inicio Restringir Reserva',}),
                               required=False)
    reservaF = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Fin Restringir Reserva',}),
                               required=False)
    
    class Meta:
        model = Estacionamiento
        fields = '__all__'


class ReservaForm(forms.ModelForm):
    estacionamiento = forms.ModelChoiceField(queryset=Estacionamiento.objects.all(),
                                             empty_label="Estacionamiento",
                                             widget=forms.Select(attrs={'class': 'form-control',}))
    horaInicio = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Inicio de la Reserva',}))
    horaFin = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Fin de la Reserva',}))
    
    class Meta:
        model = Reserva
        fields = ['horaInicio', 'horaFin',]
        
        
class PagoForm(forms.ModelForm):
    TARJETAS = (
     ('Vista', 'Vista'),
     ('Mister', 'Mister'),
     ('Xpres', 'Xpres'))
      
    nombre = forms.CharField(help_text="Nombre y Apellido: ")
    cedula = forms.IntegerField(help_text="Cédula: ")
    tipoTarjeta = forms.ChoiceField(choices=TARJETAS, help_text="Tipo de tarjeta: ")
    numeroTarjeta = forms.RegexField(help_text="Nro. Tarjeta: ", min_length=16, max_length=16,
                                     regex=r'^(\d)+$', error_message = ("Número de tarjeta no válido."))        
    
    class Meta:
        model = Pago
        fields = ['nombre', 'cedula', 'tipoTarjeta', 'numeroTarjeta',]
