#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django import forms
from estacionamientos.models import Estacionamiento, Reserva, Pago


class EstacionamientosForm(forms.ModelForm):
    nombre_duenio = forms.CharField(help_text="Nombre del dueño:")
    nombre_est = forms.CharField(help_text="Nombre del estacionamiento:")
    direccion = forms.CharField(help_text="Dirección:")
    telefono1 = forms.IntegerField(help_text="Teléfono 1:")
    telefono2 = forms.IntegerField(help_text="Teléfono 2: ", required=False)
    telefono3 = forms.IntegerField(help_text="Teléfono 3:", required=False)
    email1 = forms.EmailField(help_text="Email 1:")
    email2 = forms.EmailField(help_text="Email 2: ", required=False)
    email3 = forms.EmailField(help_text="Email 3: ", required=False)
    rif = forms.IntegerField(help_text="Rif: ")
    capacidad = forms.IntegerField(help_text="Capacidad del estacionamiento:")
    tarifa = forms.DecimalField(help_text="Tarifa del estacionamiento:",max_digits=7, decimal_places=2)
    horaI = forms.TimeField(help_text="Hora de apertura:", required=False)
    horaF = forms.TimeField(help_text="Hora de cierre:", required=False)
    reservaI = forms.TimeField(help_text="Inicio de horario de reserva restringido:", required=False)
    reservaF = forms.TimeField(help_text="Fin de horario de reserva restringido", required=False)
    
    class Meta:
        model = Estacionamiento
        fields = '__all__'


class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ['estacionamiento', 'horaInicio', 'horaFin',]
        
class PagoForm(forms.ModelForm):
    TARJETAS = (
     ('Vista', 'Vista'),
     ('Mister', 'Mister'),
     ('Xpres', 'Xpres'))
      
    nombre = forms.CharField(help_text="Nombre y Apellido: ")
    cedula = forms.IntegerField(help_text="Cédula: ")
    tipoTarjeta = forms.ChoiceField(choices=TARJETAS, help_text="Tipo de tarjeta: ")
    numeroTarjeta = forms.RegexField(min_length=16, max_length=16, regex=r'^(\d)+$',
                    error_message = ("Número de tarjeta no válido."))        

    class Meta:
        model = Pago
        fields = ['nombre', 'cedula', 'tipoTarjeta','numeroTarjeta']
