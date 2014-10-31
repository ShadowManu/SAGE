'''
Created on 29/10/2014

@author: Christhian
'''
import Estacionamiento
import time

def nuevoEst(estacionamientos):
    if len(estacionamientos) == 5:
        print("Ya han sido definidos 5 estacionamientos.")
        return estacionamientos
    
    est = Estacionamiento.Estacionamiento()    
    
    while True:
        nombreD = input("Escriba el nombre del propietario del estacionamiento: ")
        try:
            est.setNombreDuenio(nombreD)
        except Estacionamiento.MalNombre as e:
            print("El nombre " + e.nombre + " no esta permitido. \nVuelva a intentarlo.")
        else:
            break

    while True:
        nombreE = input("Escriba el nombre del estacionamiento: ")
        try:
            est.setNombreEstacionamiento(nombreE)
        except Estacionamiento.MalEstacionamiento as e:
            print("El nombre " + e.nombre + " no esta permitido. \nVuelva a intentarlo.")
        else:
            break

    while True:
        direccion = input("Escriba la direccion del estacionamiento: ")
        try:
            est.setDireccion(direccion)
        except Estacionamiento.MalDireccion as e:
            print("La direccion " + e.nombre + " no esta permitida. \nVuelva a intentarlo.")
        else:
            break
            
    while True:
        telefono = input("Introduzca un numero de telefono: ")
        try:
            est.setTelefonos(telefono)
            while True:
                telefono = input("Introduzca otro numero de telefono (para dejar de agregar numeros ingrese una linea vacia): ")
                if (telefono == ''):
                    break
                est.setTelefonos(telefono)
        except Estacionamiento.MalTelefono as t:
            print("El numero " + t.numero + " no esta escrito correctamente")
            print("Por favor introduzca solo 11 digitos, 4 del codigo mas los 7 restantes.")
            print("Vuelva a intentarlo.")
        except Estacionamiento.MaxTelefonos:
            print("Solo puede tener 3 numeros telefonicos asociados al estacionamiento")
            break
        else:
            break
            
    while True:
        email = input("Introduzca un correo electronico: ")
        try:
            est.setCorreoElectronico(email)
            while True:
                email = input("Introduzca otro correo electronico (para dejar de agregar correos presione 'enter'): ")
                if (email == ''):
                    break
                est.setCorreoElectronico(email)
        except Estacionamiento.MalCorreo as e:
            print("El correo " + e.email + " no esta escrito correctamente.")
            print("Por favor introduzca un correo electronico valido.")
            print("Vuelva a intentarlo.")
        except Estacionamiento.MaxCorreos:
            print("Solo puede tener 2 correos asociados al estacionamiento")
            break
        else:
            break

    while True:
        rif = input("Introduzca el rif: ")
        try:
            est.setRif(rif)
        except Estacionamiento.MalRif:
            print("Formato incorrecto. \nVuelva a intentarlo.")
        else:
            break

    estacionamientos.append(est)
    print("Estacionamiento agregado.\n\n")
    return estacionamientos


def printEst(estacionamientos):
    i = 1
    print("Estacionamientos en el SAGE")
    for x in estacionamientos:
        print("  ",i,".- ",x.getNombreEstacionamiento())
        i = i+1

def parametrizarEst(estacionamientos):
    if estacionamientos == []:
        print("No hay estacionamientos")
        return estacionamientos
    
    printEst(estacionamientos)
        
    while True:
        opcion = input("Ingrese el numero del estacionamiento a parametrizar:")
        try:
            est = estacionamientos[int(opcion)-1]
        except:
            print("Ingrese un numero valido.")
        else:
            break
    
    print("Estacionamiento: ", est.getNombreEstacionamiento())
    cap = input("  Ingrese la capacidad del estacionamiento: ")
    est.setCapacidad(cap)
    
    while True:
        try:
            horaAbre = input("  Ingrese el horario de apertura del estacionamiento (hh:mm am/pm): ")
            abre = time.strptime(horaAbre, "%I:%M %p")
            horaCierra = input("  Ingrese el horario de cierre del estacionamiento (hh:mm am/pm): ")
            cierra = time.strptime(horaCierra, "%I:%M %p")
            est.setHorario(abre, cierra)
        except:
            print("Ingrese la hora con el formato correcto: hh:mm am/pm.")
        else:
            break
            
    while True:
        rest = input("  Habra un horario restringido para reservas? (S/N): ")
        try:
            if rest == 'S' or rest == 's':
                inicioRest = input("  Ingrese el inicio del horario restringido (hh:mm am/pm): ")
                inicio = time.strptime(inicioRest, "%I:%M %p")
                finRest = input("  Ingrese fin del horario restringido (hh:mm am/pm): ")
                fin = time.strptime(finRest, "%I:%M %p")
                est.setHorarioReserva(inicio, fin)
                break
            elif rest == 'N' or rest == 'n':
                break
        except:
            print("Ingrese la hora con el formato correcto: hh:mm am/pm.")
        
    tarifa = input("  Ingrese la tarifa del estacionamiento: ")
    est.setTarifa(tarifa)
    estacionamientos[int(opcion)-1] = est # Falta verificar si hace falta.
    return estacionamientos

if __name__ == "__main__":

    cincoEst = []
    opciones = {'1':nuevoEst, '2':parametrizarEst}
    print ("Bienvenido al SAGE")
    print ("1.- Ingresar un nuevo estacionamiento. \n2.- Parametrizar un estacionamiento. \n3.- Salir.")
    
    while True:
                
        opcion = input ("Ingrese una opcion (1, 2 o 3): ")
        if opcion == '3':
            print("Hasta luego.")
            quit(0)
        try:
            cincoEst = opciones[opcion](cincoEst)
        except:
            print("Ingrese una opcion valida.")