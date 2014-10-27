'''
Created on 22/10/2014

@author: Jesus Adolfo Parra
@author: Edgar Valderrama
(agregar todos los demas)
'''
# placaTurno es un diccionario que relaciona las placas al turno en que llego
from helpers import *

def TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto):
    resNoOcup = 0
    resOcup = 0
    ocup = 0
    
    reservo = False
    if not (placa in placaTurno):
        return [resNoOcup,resOcup,ocup]
    
    puesto = placaPuesto[placa]
    hora_llegada = placaTurno[placa]
    
    if (estadoEstacionamiento[puesto][hora_llegada] == 3):
        reservo = True
    
    if (reservo):
        i = hora_llegada
        while (estadoEstacionamiento[puesto][i-1]):
            
            if (estadoEstacionamiento[puesto][i-1]==2):
                resNoOcup=resNoOcup+1
                
            i=i+1        
            
            
        i = horaSalida    
        
        while (estadoEstacionamiento[puesto][i+1]):
            
            if (estadoEstacionamiento[puesto][i+1]==2):
                resNoOcup=resNoOcup+1
                
            i = i + 1
            
            
        if (resNoOcup != 0):
            i = hora_llegada
            while (estadoEstacionamiento[puesto][i]):
            
                if (estadoEstacionamiento[puesto][i]==3):
                    resOcup=resOcup+1
                    
                i = i + 1
                
                            
    i = horaSalida

    while (i >= hora_llegada):
        
        if (estadoEstacionamiento[puesto][i]==1):
                ocup=ocup+1
       
        i = i - 1
        
    
    return [resNoOcup,resOcup,ocup]
    
