'''
Created on 16/10/2014

@author: Cristian Medina
'''


'''
Funcion: reservarPuesto
Entrada: 
    estacionamiento: un objeto tipo estacionamiento.
    horarioReserva: tupla con dos string que indiquen el rango de tiempo de reserva
    placa: string que indica la placa del vehiculo que desea reservar.
Salida:
    booleano indicando si se realizo la reserva.
Descripcion: dado una placa y una tupla con el rango de horario en el que se desea reservar
se devuelve un booleano indicando si se pudo reservar un puesto o no.
'''
def reservarPuesto(estacionamiento,horarioReserva,placa):
    #Solo se devuelve un booleano que indica si se pudo reservar o no un puesto.     
    puesto = estacionamiento.verificarDisponibilidad(horarioReserva[0],horarioReserva[1])
    
    if not(puesto):
        return False
    
    else:
        estacionamiento.reservar(horarioReserva[0],horarioReserva[1],placa)
        return True 
