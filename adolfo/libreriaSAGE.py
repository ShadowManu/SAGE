'''
Created on Oct 16, 2014

@author: adolfo
'''

class MyClass(object):
    '''
    classdocs
    '''    
    
    def __init__(self):
        '''
        Constructor
        '''
        num_filas = 10
    
        estadoEstacionamiento = [range(23) for i in range(num_filas)]
        for i in range(num_filas):
            for j in range(23):
                estadoEstacionamiento[i][j] = 0
        
        placaPuesto = dict()
        
        horaToBloque = dict ()
        horaToBloque ["6:00am"] = 1
        horaToBloque ["6:30am"] = 2
        horaToBloque ["7:00am"] = 3
        horaToBloque ["7:30am"] = 4
        horaToBloque ["8:00am"] = 5
        horaToBloque ["8:30am"] = 6
        horaToBloque ["9:00am"] = 7
        horaToBloque ["9:30am"] = 8
        horaToBloque ["10:00am"] = 9
        horaToBloque ["10:30am"] = 10
        horaToBloque ["11:30am"] = 11
        horaToBloque ["12:00pm"] = 12
        horaToBloque ["12:30pm"] = 13
        horaToBloque ["1:00pm"] = 14
        horaToBloque ["1:30pm"] = 15
        horaToBloque ["2:00pm"] = 16
        horaToBloque ["2:30pm"] = 17
        horaToBloque ["3:00pm"] = 18
        horaToBloque ["3:30pm"] = 19
        horaToBloque ["4:00pm"] = 20
        horaToBloque ["4:30pm"] = 21
        horaToBloque ["5:00pm"] = 22
        horaToBloque ["5:30pm"] = 23
    
        
        