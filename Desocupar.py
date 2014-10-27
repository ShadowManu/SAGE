'''
    Nombre: desocuparPuesto
    Descripcion: dado el tiempo de salida de un
    vehiculo y su placa, la funcion desocupa el puesto
    que este vehiculo ocupaba.    
'''
from helpers import *
def desocuparPuesto(
        estadoEstacionamiento,  # Estacionamiento donde se reserva el puesto
        placa,                  # Placa del vehiculo del cliente
        horaSalida,             # Hora de Salida del vehiculo.
        placaPuesto             # Lista de puestos con un vehiculo asociado
    ):
    
    if (horaSalida < 1) or (horaSalida > NUMBER_TURNS):
        print("Hora de salida invalido")
        
    else:
        if placa in placaPuesto:
            puesto = placaPuesto[placa]
            del placaPuesto[placa]
            del placaTurno[placa]
            return puesto
         
    return None