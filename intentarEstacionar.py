'''
    Nombre: intentarEstacionar
    Descripcion: debe chequear la disponibilidad de puesto
        y en caso de haberlo, asignarlo a la placa en el 
        diccionario placaPuesto y actilizar la matriz 
        marcando el puesto como ocupado.
        Se indica con un booleano si fue posible asignarle
        un puesto.
'''

def intentarEstacionar(
        estadoEstacionamiento,    # Estacionamiento donde se reserva el puesto
        placa,                    # Placa del vehiculo del cliente
        horaLlegada,              # Indica la hora de llegada al estacionamiento
        placaPuesto               # Lista de puestos con un vehiculo asociado
    ):
    
    hayPuesto = false
    for x in range(len(estadoEstacionamiento)):
        if estadoEstacionamiento[x][horaLlegada - 1] == 0:
            hayPuesto = true
            estadoEstacionamiento[x][horaLlegada - 1] == 1
            placaPuesto[placa] = x
            break

    return hayPuesto