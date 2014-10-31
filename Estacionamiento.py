'''
Created on 28/10/2014

@author: adolfo, edgar
(Agregar a todos los demas)
'''
import re
re.UNICODE

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


class MalCap(Error):
    
    def __init__(self,cap):
        self.nombre = cap
        

class MalTarifa(Error):

    def __init__(self,tarifa):
        self.nombre = tarifa


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
        if not (isinstance(nombre, str)):
            raise MalNombre(nombre)
        
        match = re.match('^[\D]+$', nombre)
        
        if ( not match):
            raise MalNombre(nombre)
        
        self.nombreDuenio = nombre        
    

    def getNombreDuenio(self):            
        return self.nombreDuenio
    

    def setNombreEstacionamiento(self,nombre):
        if not (isinstance(nombre, str)):
            raise MalEstacionamiento(nombre)
        
        if (nombre == '' ):
            raise MalEstacionamiento(nombre)
        self.nombreEstacionamiento = nombre
    

    def getNombreEstacionamiento(self):
        return self.nombreEstacionamiento
    

    def setDireccion(self,direccion):
        if not (isinstance(direccion, str)):
            raise MalDireccion(direccion)
        
        if (direccion == '' ):
            raise MalDireccion(direccion)
        self.direccion = direccion
    

    def getDireccion(self):
        return self.direccion
    

    def setTelefonos(self, telefono):
        if not (isinstance(telefono, str)):
            raise MalTelefono(telefono)
        
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
        if not (isinstance(email, str)):
            raise MalCorreo(email)
        
        if (len(self.correoElectronico) < 2) :
            match = re.match("^[a-zA-Z0-9|-|_]+@([a-zA-Z0-9|-|_]+\.)+[a-zA-Z0-9]+$",email) 
            if not match:
                raise MalCorreo(email)
            self.correoElectronico.append(email)
        else:
            raise MaxCorreos
    

    def getCorreoElectronico(self):
        return self.correoElectronico
    

    def setRif(self,rif):
        if not (isinstance(rif,str)):
            raise MalRif(rif)
        
        if (rif == '' ):
            raise MalRif(rif)
        match = re.match("^(J|j|v|V)[0-9]{10}$",rif) 
        if not match:
            raise MalRif(rif)
        self.rif = rif
    

    def getRif(self):
        return self.rif
    

    def setCapacidad(self,capacidad):
        if int(capacidad) <= 0:
            raise MalCap(int(capacidad))
        self.capacidad = capacidad
        
    

    def getCapacidad(self):
        return self.capacidad
    

    def setTarifa(self,tarifa):
        if int(tarifa) <=0:
            raise MalTarifa
        self.tarifa = tarifa
    

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
