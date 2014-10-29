'''
Created on 28/10/2014

@author: adolfo
(Agregar a todos los demas)
'''
from datetime import date, datetime, time
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
        error = False
        
        while not(error):
            nombreD = input("Escriba el nombre del propietario del estacionamiento: ")
            try:
                self.setNombreDuenio(nombreD)
            except MalNombre as e:
                print("el nombre " + e.nombre + " no esta permitido. \nUtilice solo letras.")
                print("Vuelva a intentarlo.")
            else: 
                error=True
                
        error = False
        nombreE = input("Escriba el nombre del estacionamiento: ")
        self.setNombreEstacionamiento(nombreE)
        direccion = input("Escriba la direccion del estacionamiento: ")
        self.setDireccion(direccion)
                
        while not(error):
            telefono = input("Introduzca un numero de telefono: ")
            try:
                self.setTelefonos(telefono)
                while not(error):
                    telefono = input("Introduzca otro numero de telefono (para dejar de agregar numeros ingrese una linea vacia): ")
                    if (telefono == ''):
                        error=True
                    else:
                        self.setTelefonos(telefono)
            except MalTelefono as t:
                print("El numero " + t.numero + " no esta escrito correctamente")
                print("Por favor introduzca solo 11 digitos, 4 del codigo mas los 7 restantes.")
                print("Vuelva a intentarlo.")
            except MaxTelefonos:
                print("Solo puede tener 3 numeros telefonicos asociados al estacionamiento")
                error = True
            else:
                error = True
                
        error = False
        
        while not(error):
            email = input("Introduzca un correo electronico: ")
            try:
                self.setCorreoElectronico(email)
                while not(error):
                    
                    email = input("Introduzca otro correo electronico (para dejar de agregar correos ingrese una linea vacia): ")
                    if (email == ''):
                        error=True
                    else:
                        self.setCorreoElectronico(email)
            except MalCorreo as e:
                print("El correo " + e.email + " no esta escrito correctamente")
                print("Por favor introduzca un correo electronico valido.")
                print("Vuelva a intentarlo.")
            except MaxCorreos:
                print("Solo puede tener 2 correos asociados al estacionamiento")
                error = True
            else:
                error = True
        
        rif = input("Introduzca el rif: ")
        self.setRif(rif)
        
    def setNombreDuenio(self,nombre):
        match = re.match('^[A-Za-z]+$', nombre)
        
        if ( not match):
            raise MalNombre(nombre)
        
        self.nombreDuenio = nombre        
    
    def getNombreDuenio(self):
        return self.nombreDuenio
    
    def setNombreEstacionamiento(self,nombre):
        self.nombreEstacionamiento = nombre
    
    def getNombreEstacionamiento(self):
        return self.nombreEstacionamiento
    
    def setDireccion(self,direccion):
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
    
    def setHorario(self):
        pass
    
    def getHorario(self):
        return self.horario
    
    def setHorarioReserva(self):
        pass
    
    def getHorarioReserva(self):
        return self.horario
    
if __name__ == "__main__":
    a = Estacionamiento()
    print (a.getNombreDuenio())
    
    