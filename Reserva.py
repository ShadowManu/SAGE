'''
    Nombre: reservarPuesto
    Descripcion: dado un intervalo de tiempo en el
    un cliente quisiera reservar un puesto, la funcion
    indica si es factible y reserva el puesto de existir.
    Se indica con un booleano si la reservacion fue 
    exitosa.    
'''
from helpers import NUMBER_TURNS

def reservarPuesto(
        estadoEstacionamiento,    # Estacionamiento donde se reserva el puesto
        tiempoReservado,        # Tupla con el intervalo de tiempo
        placa,                    # Placa del vehiculo del cliente
        placaPuesto                # Lista de puestos con un vehiculo asociado
    ):

    
    horaInicio = tiempoReservado[0] - 1
    horaFinal = tiempoReservado[1] - 1
    
    if ( (horaFinal < horaInicio) or (horaFinal < 0) or (horaInicio < 0) 
        or (horaFinal > NUMBER_TURNS) or (horaInicio > NUMBER_TURNS) ):
        print("Rango de hora Incorrecto")
    
    else:
        for x in range(len(estadoEstacionamiento)):
            hayPuesto = False
            if estadoEstacionamiento[x][horaInicio] == 0:
                hayPuesto = True
                for y in range(horaInicio + 1,horaFinal+1):
                    if (estadoEstacionamiento[x][y] != 0):
                        hayPuesto = False
                        break
    
                if hayPuesto:
                    placaPuesto[placa] = x
                    
                    for y in range(horaInicio,horaFinal+1):
                        estadoEstacionamiento[x][y] = 2 
    
                    return True
                
    return False
