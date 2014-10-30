'''
Created on 28/10/2014

@author: adolfo, edgar
(Agregar a todos los demas)
'''
import time
import re


class Error(Exception):
    pass


class MalNombre(Error):
    
    def __init__(self, nombre):
        self.nombre = nombre
        

class MalTelefono(Error):
    
    def __init__(self, numero):
        self.numero = numero
        

class MalCorreo(Error):
    
    def __init__(self, email):
        self.email = email


class MalEstacionamiento(Error):

    def __init__(self,nombre):
        self.nombre = nombre
        

class MalDireccion(Error):

    def __init__(self,direccion):
        self.nombre = direccion
        

class MalRif(Error):
    
    def __init__(self,rif):
        self.nombre = rif


class MaxTelefonos(Error):
    pass


class MaxCorreos(Error):
    pass


class Estacionamiento(object):
    '''
    Clase para los estacionamientos
    '''
    nombreDuenio = ''
    nombreEstacionamiento = ''
    direccion = ''
    telefonos = []
    correoElectronico = []
    rif = ''
    capacidad = 0
    tarifa = 0
    horario = []
    horarioReserva = [] 


    def __init__(self):
        '''
        Constructor
        '''
       

    def setNombreDuenio(self,nombre):
        match = re.match('^[A-Za-z]+$', nombre)
        
        if ( not match):
            raise MalNombre(nombre)
        
        self.nombreDuenio = nombre        
    

    def getNombreDuenio(self):
        return self.nombreDuenio
    

    def setNombreEstacionamiento(self,nombre):
        if (nombre == '' ):
            raise MalEstacionamiento
        self.nombreEstacionamiento = nombre
    

    def getNombreEstacionamiento(self):
        return self.nombreEstacionamiento
    

    def setDireccion(self,direccion):
        if (direccion == '' ):
            raise MalDireccion
        self.direccion = direccion
    

    def getDireccion(self):
        return self.direccion
    

    def setTelefonos(self, telefono):
        if (len(self.telefonos) < 3) :
            match = re.match("^[0-9]{11}$", telefono) 
            if not match:
                raise MalTelefono(telefono)
            self.telefonos.append(telefono)
        else:
            raise MaxTelefonos
    

    def getTelefonos(self):
        return self.telefonos


    def setCorreoElectronico(self, email):
        if (len(self.correoElectronico) < 2) :
            match = re.match("^[a-z0-9]+@([a-z0-9]+\.)+[a-z0-9]+$",email) 
            if not match:
                raise MalCorreo(email)
            self.correoElectronico.append(email)
        else:
            raise MaxCorreos
    

    def getCorreoElectronico(self):
        return self.correoElectronico
    

    def setRif(self,rif):
        # Falta verificar los rif
        if (rif == '' ):
            raise MalRif
        self.rif = rif
    

    def getRif(self):
        return self.rif
    

    def setCapacidad(self,capacidad):
        self.capacidad = int(capacidad)
    

    def getCapacidad(self):
        return self.capacidad
    

    def setTarifa(self,tarifa):
        self.tarifa = int(tarifa)
    

    def getTarifa(self):
        return self.tarifa
    

    def setHorario(self, abre, cierra):
        self.horario.append(abre)
        self.horario.append(cierra)
    
    
    def getHorario(self):
        return self.horario
    
    
    def setHorarioReserva(self, abre, cierra):
        self.horarioReserva.append(abre)
        self.horarioReserva.append(cierra)
    
    
    def getHorarioReserva(self):
        return self.horario 


'''
    Funciones para declarar un estacionamiento nuevo
    o parametrizar uno ya existente.
'''
def nuevoEst(estacionamientos):
    if len(estacionamientos) == 5:
        print("Ya han sido definidos 5 estacionamientos.")
        return estacionamientos
    else:
        ''' ACA DEBERIA IR EL CREAR ESTACIONAMIENTO PERO COMO ADOLFO LO BORRO NO SE'''
        est = Estacionamiento()
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
    
    while (True):
        print ("Bienvenido al SAGE")
        opciones = {'1': nuevoEst, '2': parametrizarEst}
        print ("1.- Ingresar un nuevo estacionamiento. \n2.- Parametrizar un estacionamiento. \n3.- Salir.")
        opcion = input("Ingrese una opcion (1, 2 o 3): ")
        
        if opcion == "3":
            print("Hasta luego.")
            break
        
        try:
            opciones[opcion](cincoEst)
        except:
            print("Ingrese una opcion valida.")    