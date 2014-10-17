'''
Created on 16/10/2014

@author: Cristian Medina
'''

'''
Funcion: desocuparPuesto
Entrada: 
    estacionamiento: un objeto tipo estacionamiento.
    horarioReserva: tupla con dos string que indiquen el rango de tiempo de reserva
    placa: string que indica la placa del vehiculo que desea reservar.
Salida:
    booleano indicando si se realizo la reserva.
Descripcion: dado una placa y una tupla con el rango de horario en el que se desea reservar
se devuelve un booleano indicando si se pudo reservar un puesto o no.
'''
def desocuparPuesto(estacionamiento,horarioSalida,placa):
    puesto = estacionamiento.buscarPlaca(placa)
    if not(puesto):
        return
    else:
        estacionamiento.desocuparPuesto(puesto)
        return
    