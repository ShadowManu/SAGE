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
    else:
        est = Estacionamiento.Estacionamiento()
        error = False
        
        while not(error):
            nombreD = input("Escriba el nombre del propietario del estacionamiento: ")
            try:
                est.setNombreDuenio(nombreD)
            except Estacionamiento.MalNombre as e:
                print("el nombre " + e.nombre + " no esta permitido. \nUtilice solo letras.")
                print("Vuelva a intentarlo.")
            else: 
                error=True
                
        error = False
        nombreE = input("Escriba el nombre del estacionamiento: ")
        est.setNombreEstacionamiento(nombreE)
        direccion = input("Escriba la direccion del estacionamiento: ")
        est.setDireccion(direccion)
                
        while not(error):
            telefono = input("Introduzca un numero de telefono: ")
            try:
                est.setTelefonos(telefono)
                while not(error):
                    telefono = input("Introduzca otro numero de telefono (para dejar de agregar numeros ingrese una linea vacia): ")
                    if (telefono == ''):
                        error=True
                    else:
                        est.setTelefonos(telefono)
            except Estacionamiento.MalTelefono as t:
                print("El numero " + t.numero + " no esta escrito correctamente")
                print("Por favor introduzca solo 11 digitos, 4 del codigo mas los 7 restantes.")
                print("Vuelva a intentarlo.")
            except Estacionamiento.MaxTelefonos:
                print("Solo puede tener 3 numeros telefonicos asociados al estacionamiento")
                error = True
            else:
                error = True
                
        error = False
        
        while not(error):
            email = input("Introduzca un correo electronico: ")
            try:
                est.setCorreoElectronico(email)
                while not(error):
                    
                    email = input("Introduzca otro correo electronico (para dejar de agregar correos ingrese una linea vacia): ")
                    if (email == ''):
                        error=True
                    else:
                        est.setCorreoElectronico(email)
            except Estacionamiento.MalCorreo as e:
                print("El correo " + e.email + " no esta escrito correctamente")
                print("Por favor introduzca un correo electronico valido.")
                print("Vuelva a intentarlo.")
            except Estacionamiento.MaxCorreos:
                print("Solo puede tener 2 correos asociados al estacionamiento")
                error = True
            else:
                error = True
        
        rif = input("Introduzca el rif: ")
        est.setRif(rif)
        estacionamientos.append(est)
        print("Estacionamiento agregado.\n")
    return estacionamientos


def printEst(estacionamientos):
    i = 1
    print("Estacionamientos en el SAGE")
    for x in estacionamientos:
        print("  ",i,".- ",x.nombreEstacionamiento)
        i = i+1

def parametrizarEst(estacionamientos):
    if estacionamientos == []:
        print("No hay estacionamientos")
        return
    printEst(estacionamientos)
        
    while True:
        try:
            opcion = input("Ingrese el numero del estacionamiento a parametrizar:")
            est = estacionamientos[int(opcion)-1]
            break
        except:
            print("Ingrese un numero valido.")
    
    print("Estacionamiento: ", est.nombreEstacionamiento)
    cap = input("  Ingrese la capacidad del estacionamiento: ")
    est.setCapacidad(cap)
    
    while True:
        try:
            horaAbre = input("  Ingrese el horario de apertura del estacionamiento (hh:mm am/pm): ")
            abre = time.strptime(horaAbre, "%I:%M %p")
            horaCierra = input("  Ingrese el horario de cierre del estacionamiento (hh:mm am/pm): ")
            cierra = time.strptime(horaCierra, "%I:%M %p")
            est.setHorario(abre, cierra)
            break
        except:
            print("Ingrese la hora con el formato correcto: hh:mm am/pm.")
            
    while True:
        try:
            rest = input("  Habra un horario restringido para reservas? (S/N): ")
            if rest == 'S' or rest == 's':
                inicioRest = input("  Ingrese el inicio del horario restringido (hh:mm am/pm): ")
                inicio = time.strptime(inicioRest, "%I:%M %p")
                finRest = input("  Ingrese fin del horario restringido (hh:mm am/pm): ")
                fin = time.strptime(finRest, "%I:%M %p")
                est.setHorarioReserva(inicio, fin)
            elif rest == 'N' or rest == 'n':
                break
            else:
                continue
        except:
            print("Ingrese la hora con el formato correcto: hh:mm am/pm.")
        
    tarifa = input("  Ingrese la tarifa del estacionamiento: ")
    est.setTarifa(tarifa)

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
            opciones[opcion](cincoEst)
        except:
            print("Ingrese una opcion valida.")