'''
Created on 16/10/2014

@author: zurdorod
'''
from errno import ESTALE

class UtilitysSAGE(object):
    '''
    classdocs
    '''    
    num_filas = 10
    placaPuesto = dict()
    horaToBloque = dict ()
    estadoEstacionamiento = [range(24) for i in range(num_filas)]
    
    def __init__(self):
        '''
        Constructor
        '''
    
        for i in range(self.num_filas):
            for j in range(24):
                self.estadoEstacionamiento[i][j] = 0
        
        self.horaToBloque ["6:00am"] = 0
        self.horaToBloque ["6:30am"] = 1
        self.horaToBloque ["7:00am"] = 2
        self.horaToBloque ["7:30am"] = 3
        self.horaToBloque ["8:00am"] = 4
        self.horaToBloque ["8:30am"] = 5
        self.horaToBloque ["9:00am"] = 6
        self.horaToBloque ["9:30am"] = 7
        self.horaToBloque ["10:00am"] = 8
        self.horaToBloque ["10:30am"] = 9
        self.horaToBloque ["11:00am"] = 10
        self.horaToBloque ["11:30am"] = 11
        self.horaToBloque ["12:00pm"] = 12
        self.horaToBloque ["12:30pm"] = 13
        self.horaToBloque ["1:00pm"] = 14
        self.horaToBloque ["1:30pm"] = 15
        self.horaToBloque ["2:00pm"] = 16
        self.horaToBloque ["2:30pm"] = 17
        self.horaToBloque ["3:00pm"] = 18
        self.horaToBloque ["3:30pm"] = 19
        self.horaToBloque ["4:00pm"] = 20
        self.horaToBloque ["4:30pm"] = 21
        self.horaToBloque ["5:00pm"] = 22
        self.horaToBloque ["5:30pm"] = 23
    
        
    def verificarDisponibilidad (self, inicio, fin):
        '''
        Verifica si hay puestos disponibles en el rango
        [inicio..fin). Retorna el primer puesto con dicha
        disponibilidad. En caso de no haber disponibilidad retorna -1.
        '''
        hay = -1
        if fin - inicio > 1:
            for i in range(self.num_filas):
                for j in range(inicio,fin):
                    if self.estadoEstacionamiento[i][j] > 0:
                        continue
                if j == fin-1:
                    hay = i
                    break
        else:
            for i in range(self.num_filas):
                if self.estadoEstacionamiento[i][inicio] == 0:
                    hay = i
                    break
        return hay

    def reservar (self, inicio, fin, placa):
        '''
        Realiza la reserva de un puesto (si esta disponible) en el 
        horario indicado por el rango [inicio..fin)
        '''
        if not placa in self.placaPuesto: # verifica que no intente ingresar 2 veces una misma placa
            inic = self.horaToBloque[inicio]
            fi = self.horaToBloque[fin]
            lugar = self.verificarDisponibilidad(inic, fi) 
            if lugar != -1:
                for i in range(self.horaToBloque[inicio],self.horaToBloque[fin]):
                    self.estadoEstacionamiento[lugar][i] = 2
                self.placaPuesto[placa] = lugar
            else:
                return False
            return True
        return False
    
    def estacionar (self, inicio, placa):
        '''
        Verifica si hay un puesto disponible y lo reserva
        '''
        if not placa in self.placaPuesto:
            lugar = self.verificarDisponibilidad(self.horaToBloque[inicio],self.horaToBloque[inicio]+1)
            if lugar != -1:
                self.estadoEstacionamiento[lugar][self.horaToBloque[inicio]] = 1
                self.placaPuesto[placa] = lugar
                return True
            return False
        return False

    

# estas son pruebas
a = UtilitysSAGE()
print(a.reservar("6:00am", "10:30am", "12345"))
print(a.reservar("6:00am", "10:30am", "12345"))
print(a.reservar("6:00am", "6:30am", "otra"))
print(a.estacionar("7:00am","54321"))
print(a.estadoEstacionamiento)
print(a.placaPuesto)


