'''
Created on 16/10/2014

@author: Christhian

Funcion: TiempoACobrar
Entrada: 
    estadoEstacionamiento:
    placa: string que indica la placa del vehiculo que desea reservar.
    tiempoSalida:
    placaPuesto: 
Salida:
    unidadesReservadoNoOcupado: Tiempo reservado no ocupado
    unidadesReservadoOcupado: Tiempo reservado Ocupado
    unidadesOcupado: Tiempo Ocupado
Descripcion: Al salir un cliente del estacionamiento, esta función calcula 
el tiempo que ha permanecido estacionado independientemente de si es un cliente 
con reserva o imprevisto.
'''

def TiempoACobrar(estadoEstacionamiento, placa, tiempoSalida, placaPuesto):
    
    puesto = placaPuesto.get(placa)
    if puesto == None:
        return None
        
        
    salida = {"unidadesReservadoNoOcupado": reservadoNoOcupado,
              "unidadesReservadoOcupado"  : reservadoOcupado,
              "unidadesOcupado"           : TiempoOcupado}    #reservadoNoOcupado, reservadoOcupado y TiempoOcupado
    return
        
    
    
    
    
     
        