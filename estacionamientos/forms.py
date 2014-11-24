#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django import forms
from estacionamientos.models import Estacionamiento, Reserva, Pago


class EstacionamientosForm(forms.ModelForm):
    nombre_duenio = forms.RegexField(help_text="Nombre del dueño:",min_length=1, max_length=20, regex=r'[^\W\d_]+$',
                    error_message = ("El dueno debe contener un nombre valido (Solo caracteres y espacios)."))
    
    nombre_est = forms.CharField(help_text="Nombre del estacionamiento:")
    
    direccion = forms.CharField(help_text="Dirección:")
    
    telefono1 = forms.RegexField(help_text="Teléfono 1:", min_length=11, max_length=11, regex=r'(0212|0412|0416|0414|0426)\d{7}$',
               error_message = ("El telefono tiene que tener el formato correcto y ser solo números (0xxx-xxxxxxx) y solo telefonos de caracas o celulares."))
    
    telefono2 = forms.RegexField(help_text="Teléfono 2: ", required=False, min_length=11, max_length=11, regex=r'(0212|0412|0416|0414|0426)-\d{7}$',
                error_message = ("El telefono tiene que tener el formato correcto y ser solo números (0xxx-xxxxxxx) y solo telefonos de caracas o celulares."))
    
    telefono3 = forms.RegexField(help_text="Teléfono 3:", required=False, min_length=11, max_length=11, regex=r'(0212|0412|0416|0414|0426)-\d{7}$',
               error_message = ("El telefono tiene que tener el formato correcto y ser solo números (0xxx-xxxxxxx) y solo telefonos de caracas o celulares."))
    
    email1 = forms.RegexField(help_text="Email 1:", regex=r'[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$',
                    error_message = ("El email tiene que tener el formato correcto."))
    
    email2 = forms.RegexField(help_text="Email 2: ", required=False, regex=r'[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$',
                  error_message = ("El email tiene que tener el formato correcto."))
    
    email3 = forms.RegexField(help_text="Email 3: ", required=False, regex=r'[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$',
                 error_message = ("El email tiene que tener el formato correcto."))
    
    rif = forms.RegexField(help_text="Rif: ", regex=r'[0-9]{9}$', error_message = ("El rif tiene que tener el formato correcto, una letra y nueve digitos."))
    
    capacidad = forms.IntegerField(help_text="Capacidad del estacionamiento:")
    
    tarifa = forms.IntegerField(help_text="Tarifa del estacionamiento:")
    
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
