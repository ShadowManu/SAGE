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
        
                      
    
    #39Prueba de none dueño
        
    def testsetNombreDuenioNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(None) 
    
    #40Prueba de Otro tipo
       
    def testsetNombreDuenioOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(3) 
    
    
    #41 Prueba de nombre dueño vacío
        
    def testsetNombreDuenioVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("")
            
    
    #42 Prueba de nombre dueño min
       
    def testsetNombreDuenioMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("a")
   
    
    #43 Prueba de nombre dueño Inválido simple
        
    def testsetNombreDuenioInvalidoSimple(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("3")
   
    
    #44 Prueba de nombre dueño Aceptable
        
    def testsetNombreDuenioAceptable(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ana")  
            
    
    #45 Prueba de nombre dueño con acento y ñ
        
    def testsetNombreDuenioAcento(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ángelañ")
            
    
    #46 Prueba de nombre dueño caracteres combinados
        
    def testsetNombreDuenioCombinado(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("rgewttrt?$#$FFS365ds63ffdffd63:8797343")         
              
            
    
    #47 Prueba de nombre dueño EXTREMO
        
    def testsetNombreDuenioExtremo(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("AaaaAFFDddsdIUUUUññññÑÑñúúúúúúááéééíííÍÍÁÁÁÚÚÚíóóóóüüüüüÜÜÜÜÓÓÓÓÓÓÉÉEÉ")


    #48 Prueba de getNombreDuenio
       
    def testgetNombre(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ana")
        self.assertEqual("Ana",Estacionam.getNombreDuenio())   
            
    
    #49 Prueba de none Direccion
        
    def testsetDireccionNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion(None) 
    
    #50 Prueba de otro tipo
        
    def testsetDireccionOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion(True)
    
    
    #51 Prueba de Direccion vacía
       
    def testsetDireccionVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion("")
            
    
    #52 Prueba de Direccion Mínima
        
    def testsetDireccionMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("a")
   
   
    
    #51 Prueba de Dirección aceptabe
        
    def testsetDireccionAceptable(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("El paraíso, Av. Paéz, Edif Tutuá, Planta Baja 1")  
            
            
    
    #53 Prueba de Dirección EXTREMA
        
    def testsetDireccionExtrema(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("AaaaAFFDddsdIUUUUññññÑÑÑñúúúúúúááéééíííÍÍÁÁÁÚÚÚíóóóóüüüüüÜÜÜÜÓÓÓÓÓÓÉÉEÉ")

    
    #54 Prueba de getDirección
      
    def testgetDireccion(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("El paraíso, Av. Páez, Edif Tutuá, Planta Baja 1")
        self.assertEqual("El paraíso, Av. Páez, Edif Tutuá, Planta Baja 1",Estacionam.getDireccion())   

    
    #55 Prueba de none de Correo
        
    def testsetCorreoNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico(None)
    
    
    #56 Prueba de Otro tipo
        
    def testsetCorreoOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico(0) 
       
    
    #57 Prueba Correo vacío
       
    def testsetCorreoVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("")
            
    
    #58 Prueba de Correo mínimo
       
    def testsetCorreoMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setCorreoElectronico("a@a.a")

   
    
    #59 Prueba de Correo sin @
       
    def testsetCorreoSinArroba(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("a.a")
    
    
    #60 Prueba de Correo sin .
       
    def testsetCorreoSinPunto(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("a@a")
   
            
    
    #61 Prueba de correo con caracter invalido
       
    def testsetCorreoCaracterInvalido(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("%@ko.b")         
              
            
    
    #62 Prueba de solamente @ y .
        
    def testsetCorreoArrobaPunto(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("@.")
            
    
    #63 Prueba Extrema
        
    def testsetCorreoExtremo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("yyuu898_____-----hjhj2323@hjhjkjk.ko")

            
    
    #64 Prueba Agregar más de 2 correos
        
    def testsetMasDosCorreos(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("foo@foo.foo")
            Estacionam.setCorreoElectronico("fii@fii.fii")
            Estacionam.setCorreoElectronico("fuu@fuu.fuu")
    
    #65 Prueba de getCorreo
       
    def testgetCorreo(self):
        Estacionam = Estacionamiento()
        Estacionam.setCorreoElectronico("luisitoelmalandrito@hotmail.com")
        self.assertEqual(["luisitoelmalandrito@hotmail.com"],Estacionam.getCorreoElectronico())

    
    #66 Prueba de none capacidad
        
    def testsetCapacidad(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad(None) 
    
    #67 Prueba de Otro tipo
        
    def testsetCapacidadOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad("hola") 
    
    
    #68 Prueba de nombre dueño vacío
        
    def testsetCapacidadVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad("")
            
    
    #69 Prueba de Capacidad min
       
    def testsetCapacidadMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setCapacidad("1")
   
    
    #70 Prueba de Capacidad Inválido simple
        
    def testsetCapacidadInvalido(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad(-1)
   
    
    #71 Prueba de máximo Int
        
    def testsetCapacidadMax(self):
        Estacionam = Estacionamiento()
        Estacionam.setCapacidad(sys.maxint)  
            

    
    #72 Prueba de getNombreDuenio
      
    def testgetCapacidad(self):
        Estacionam = Estacionamiento()
        Estacionam.setCapacidad(54645356)
        self.assertEqual(54645356,Estacionam.getCapacidad())
        
        
           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()