 # -*- coding: utf-8 -*-
'''
Created on Sep 29, 2014

@author: caicedodavid
'''
import unittest
from Estacionamiento import Estacionamiento
from Estacionamiento import MalNombre
import sys
'''
Clase de pruebas para el metodo Empaquetar del archivo p80910123
'''

class TestEstacionamiento(unittest.TestCase):
    
    '''
    Prueba de none
    '''    
    def testsetNombreDuenioNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(none) 
    
    '''
    Prueba de nombre vacío
    '''    
    def testsetNombreDuenioVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("")
            
    '''
    Prueba de nombre min
    '''    
    def testsetNombreDuenioMin(self):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("a")
   
    '''
    Prueba de nombre Inválido simple
    '''    
    def testsetNombreDuenioInvalidoSimple(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("3")
   
    '''
    Prueba de nombre Aceptable
    '''    
    def testsetNombreDuenioAceptable(self):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("Ana")  
            
    '''
    Prueba de nombre con acento
    '''    
    def testsetNombreDuenioAcento(self):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("Ángel")
            
    '''
    Prueba de nombre con ñ
    '''    
    def testsetNombreDuenioConEnie(self):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("Toño")         
              
              
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()