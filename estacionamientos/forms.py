#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django import forms
from estacionamientos.models import Estacionamiento


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
    tarifa = forms.IntegerField(help_text="Tarifa del estacionamiento:")
    horaI = forms.TimeField(help_text="Hora de apertura:", required=False)
    horaF = forms.TimeField(help_text="Hora de cierre:", required=False)
    reservaI = forms.TimeField(help_text="Inicio de horario de reserva restringido:", required=False)
    reservaF = forms.TimeField(help_text="Fin de horario de reserva restringido", required=False)
    
    class Meta:
        model = Estacionamiento
        fields = '__all__'