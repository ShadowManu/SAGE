'''
Created on 17/10/2014

@author: zurdorod
'''
from libreriaSAGE2 import UtilitysSAGE

a = UtilitysSAGE()
    
class SAGE(object):
    '''
    classdocs
    '''
    

    
    def reservarPuesto (self, horaInicio, horaFin, placa):
        a.reservar(horaInicio, horaFin, placa)
        
    def intentarEstacionar (self, horaLlegada, placa):
        a.estacionar(horaLlegada, placa)
        
    def tiempoACobrar(self, placa, tiempoSalida):
        a.cobrar(tiempoSalida, placa)


    def __init__(self, params):
        '''
        Constructor
        '''
        