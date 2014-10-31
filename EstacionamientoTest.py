 # -*- coding: utf-8 -*-
'''
Created on Sep 29, 2014

@author: caicedodavid
'''
import unittest
from Estacionamiento import Estacionamiento
import sys


class TestEstacionamiento(unittest.TestCase):
    
    '''
    Prueba de none dueño
    '''    
    def testsetNombreDuenioNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(none) 
    '''
    Prueba de Otro tipo
    '''    
    def testsetNombreDuenioOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(3) 
    
    '''
    Prueba de nombre dueño vacío
    '''    
    def testsetNombreDuenioVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("")
            
    '''
    Prueba de nombre dueño min
    '''    
    def testsetNombreDuenioMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("a")
   
    '''
    Prueba de nombre dueño Inválido simple
    '''    
    def testsetNombreDuenioInvalidoSimple(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("3")
   
    '''
    Prueba de nombre dueño Aceptable
    '''    
    def testsetNombreDuenioAceptable(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ana")  
            
    '''
    Prueba de nombre dueño con acento y ñ
    '''    
    def testsetNombreDuenioAcento(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ángelañ")
            
    '''
    Prueba de nombre dueño caracteres combinados
    '''    
    def testsetNombreDuenioCombinado(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("rgewttrt?$#$FFS365ds63ffdffd63:8797343")         
              
            
    '''
    Prueba de nombre dueño EXTREMO
    '''    
    def testsetNombreDuenioExtremo(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("AaaaAFFDddsdIUUUUññññÑÑñúúúúúúááéééíííÍÍÁÁÁÚÚÚíóóóóüüüüüÜÜÜÜÓÓÓÓÓÓÉÉEÉ")

    '''
    Prueba de getNombreDuenio
    '''   
    def testgetNombre(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ana")
        self.assertEqual("Ana",Estacionam.getNombreDuenio())   
            
    '''
    Prueba de none Direccion
    '''    
    def testsetDireccionNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion(none) 
    '''
    Prueba de otro tipo
    '''    
    def testsetDireccionOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion(True)
    
    '''
    Prueba de Direccion vacía
    '''    
    def testsetDireccionVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion("")
            
    '''
    Prueba de Direccion Mínima
    '''    
    def testsetDireccionMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("a")
   
   
    '''
    Prueba de Dirección aceptabe
    '''    
    def testsetDireccionAceptable(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("El paraíso, Av. Paéz, Edif Tutuá, Planta Baja 1")  
            
            
    '''
    Prueba de Dirección EXTREMA
    '''    
    def testsetDireccionExtrema(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("AaaaAFFDddsdIUUUUññññÑÑÑñúúúúúúááéééíííÍÍÁÁÁÚÚÚíóóóóüüüüüÜÜÜÜÓÓÓÓÓÓÉÉEÉ")

    '''
    Prueba de getDirección
    '''   
    def testgetDireccion(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("El paraíso, Av. Páez, Edif Tutuá, Planta Baja 1")
        self.assertEqual("El paraíso, Av. Páez, Edif Tutuá, Planta Baja 1",Estacionam.getDireccion())   

    '''
    Prueba de none de Correo
    '''    
    def testsetCorreoNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico(none)
    
    '''
    Prueba de Otro tipo
    '''    
    def testsetCorreoOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico(0) 
       
    '''
    Prueba Correo vacío
    '''    
    def testsetCorreoVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElctronico("")
            
    '''
    Prueba de Correo mínimo
    '''    
    def testsetCorreoMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setCorreoElectronico("a@a.a")

   
    '''
    Prueba de Correo sin @
    '''    
    def testsetSinArroba(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("a.a")
    
    '''
    Prueba de Correo sin .
    '''    
    def testsetSinPunto(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("a@a")
   
            
    '''
    Prueba de correo con caracter invalido
    '''    
    def testsetNombreDuenioCombinado(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("%@ko.b")         
              
            
    '''
    Prueba de solamente @ y .
    '''    
    def testsetNombreDuenioExtremo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("@.")
            
    '''
    Prueba Extrema
    '''    
    def testsetCorreoExtremo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("yyuu898_____-----hjhj2323@hjhjkjk.ko")

    '''
    Prueba de getCorreo
    '''   
    def testgetCorreo(self):
        Estacionam = Estacionamiento()
        Estacionam.setCorreoElectronico("luisitoelmalandrito@hotmail.com")
        self.assertEqual("luisitoelmalandrito@hotmail.com",Estacionam.getCorreoElectronico())  
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
   
    unittest.main()