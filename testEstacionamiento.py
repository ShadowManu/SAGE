# -*- coding: utf-8 -*-
'''
Created on Sep 29, 2014

@author: caicedodavid
@author: Jhon Villamizar
todos los demas
'''
import unittest
from Estacionamiento import Estacionamiento
from Estacionamiento import MalNombre
import sys
'''
Clase de pruebas para el metodo Empaquetar del archivo p80910123
'''

class testEstacionamiento(unittest.TestCase):
    
    '''
    Prueba de none
    '''    
    def testsetNombreDuenioNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(None) 
    
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
    
              
    def setUp(self):
        pass


    def tearDown(self):
        pass


    # 1. Colocar nombre estacionamiento vacio
    def test_setNEstVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setNombreEstacionamiento("")
        
        
    # 2. Colocar nombre estacionamiento no creado
    def test_setNEstNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setNombreEstacionamiento(None)
    
    # 3. Colocar nombre estacionamiento solo 1 numero
    def test_setNEstSoloNum(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("1")
        
       
    # 4. Colocar nombre estacionamiento solo signos 
    def test_setNEstSignos(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("-.:,")
        
      
    # 5. Colocar nombre estacionamiento otro tipo de objeto  
    def test_setNEstObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setNombreEstacionamiento([1])
        
    
    # 6. Colocar nombre estacionamiento con caracteres especiales
    def test_setNEstCarEsp(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("Buen Año")
        
     
    # 7. Colocar nombre estacionamiento con acentos   
    def test_setNEstAcentos(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("María & José")
        
     
    # 8. Colocar nombre estacionamiento correcto   
    def test_setNEstBuenC(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("Carlos y Asociados S.A")
        
        
    # 9. Colocar telefono de estacionamiento vacio    
    def test_setTlfnVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos('')
        
     
    # 10. Colocar telefono de estacionamiento no creado   
    def test_setTlfNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos(None)
        
    
    # 11. Colocar telefono de estacionamiento menor a su tamanio    
    def test_setTlfnMenorTamanio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("0212555555")
        
        
    # 12. Colocar telefono de estacionamiento solo un numero    
    def test_setTlfnSoloUno(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("4")
        
        
    # 13. Colocar telefono de estacionamiento mayor a su tamanio   
    def test_setTlfnMayorTamanio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("021255555555")
        

    # 14. Colocar telefono de estacionamiento con signos    
    def test_setTlfnSignos(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("0212555-555")
        
     
    # 15. Colocar telefono de estacionamiento otro objeto   
    def test_setTlfnObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("0212-555-55-55")
        
     
    # 16. Colocar telefono de estacionamiento de forma correcta   
    def test_setTlfnBuenC(self):
        oEst = Estacionamiento()
        oEst.setTelefonos("02124511234")
        
        
    # 17. Colocar rif vacio   
    def test_setRifVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif('')
        
    
    # 18. Colocar rif no creado      
    def test_setRifNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif(None)
        
    
    # 19. Colocar rif con solo signos de puntuacion      
    def test_setRifSignos(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif("-.,><")
        
        
    # 20. Colocar rif otro objeto      
    def test_setRifObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif(1234)
        
        
    # 21. Colocar rif con caracteres especiales     
    def test_setRifCarEsp(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif('V-1122ñ')
        
        
    # 22. Colocar rif de forma correcta     
    def test_setRifBuenC(self):
        oEst = Estacionamiento()
        oEst.setRif('J1112223334')
        
    
    # 23. Colocar tarifa vacia      
    def test_setTarifaVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa('')
        
    
    # 24. Colocar tarifa no creada     
    def test_setTarifaNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa(None)
        
    
    # 25. Colocar tarifa de otro objeto      
    def test_setTarifaObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa("Tarifa")
            
    # 27. Colocar tarifa negativa      
    def test_setTarifaNegativo(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa(-20)
        
    # 29. Colocar tarifa de forma correcta  
    def test_setTarifaBuenC(self):
        oEst = Estacionamiento()
        oEst.setTarifa(15)
        
    # 38. Colocar horario de reserva de forma correcta               
    def test_setHoraRBuenC(self):
        oEst = Estacionamiento()
        oEst.setHorarioReserva("09:00 am", "03:00 pm")
        
           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()