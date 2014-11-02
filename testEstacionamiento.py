# -*- coding: utf-8 -*-
'''
Created on 29/10/2014

@author: Caicedo David 
         Guevara Christhian
         Medina Cristian
         Pacheco Manuel
         Parra Jesus
         Valderrama Edgar
         Villamizar Jhon
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
    
    
    #1. Prueba de none due�o
    def testsetNombreDuenioNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(None) 
    
    
    #2. Prueba de Otro tipo
    def testsetNombreDuenioOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio(3) 
    
    
    #3. Prueba de nombre due�o vac�o
    def testsetNombreDuenioVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("")
            
    
    #4. Prueba de nombre due�o min
    def testsetNombreDuenioMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("a")
   
    
    #5. Prueba de nombre due�o Inv�lido simple
    def testsetNombreDuenioInvalidoSimple(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("3")
   
    
    #6. Prueba de nombre due�o Aceptable
    def testsetNombreDuenioAceptable(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ana")  
            
    
    #7. Prueba de nombre due�o con acento y �
    def testsetNombreDuenioAcento(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ángel")
            
    
    #8. Prueba de nombre due�o caracteres combinados
    def testsetNombreDuenioCombinado(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setNombreDuenio("rgewttrt?$#$FFS365ds63ffdffd63:8797343")         
              
            
    #9. Prueba de nombre due�o EXTREMO
    def testsetNombreDuenioExtremo(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("AaaaAFFDddsdIUUUU���������������������������������������������������E�")

    
    #10. Prueba de getNombreDuenio
    def testgetNombre(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreDuenio("Ana")
        self.assertEqual("Ana",Estacionam.getNombreDuenio())   


    # 11. Colocar nombre estacionamiento vacio
    def test_setNEstVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setNombreEstacionamiento("")
        
        
    # 12. Colocar nombre estacionamiento no creado
    def test_setNEstNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setNombreEstacionamiento(None)
    
    # 13. Colocar nombre estacionamiento solo 1 numero
    def test_setNEstSoloNum(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("1")
        
       
    # 14. Colocar nombre estacionamiento solo signos 
    def test_setNEstSignos(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("-.:,")
        
      
    # 15. Colocar nombre estacionamiento otro tipo de objeto  
    def test_setNEstObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setNombreEstacionamiento([1])
        
    
    # 16. Colocar nombre estacionamiento con caracteres especiales
    def test_setNEstCarEsp(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("Buen Año")
        
     
    # 17. Colocar nombre estacionamiento con acentos   
    def test_setNEstAcentos(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("María & José")
        
     
    # 18. Colocar nombre estacionamiento correcto   
    def test_setNEstBuenC(self):
        oEst = Estacionamiento()
        oEst.setNombreEstacionamiento("Carlos y Asociados S.A")
        
    
    #19. Obtener nombre de estacionamiento con la funcion get   
    def testgetNombreEstacionamiento(self):
        Estacionam = Estacionamiento()
        Estacionam.setNombreEstacionamiento("AnaMari")
        self.assertEqual("AnaMari",Estacionam.getNombreEstacionamiento())  
        
        
    #20 Prueba de none Direccion
    def testsetDireccionNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion(None) 
    
    
    #21 Prueba de otro tipo
    def testsetDireccionOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion(True)
    
    
    #22 Prueba de Direccion vac�a
    def testsetDireccionVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setDireccion("")
            
    
    #23 Prueba de Direccion M�nima
    def testsetDireccionMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("a")
   
   
    #24 Prueba de Direcci�n aceptabe
    def testsetDireccionAceptable(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("El paraíso, Av. Paéz, Edif Tutué, Planta Baja 1")  
            
            
    #25 Prueba de Direcci�n EXTREMA
    def testsetDireccionExtrema(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("AaaaAFFDddsdIUUUU����������������������������������������������������E�")

    
    #26 Prueba de getDirecci�n
    def testgetDireccion(self):
        Estacionam = Estacionamiento()
        Estacionam.setDireccion("El paraíso, Av. Paéz, Edif Tutué, Planta Baja 1")
        self.assertEqual("El paraíso, Av. Paéz, Edif Tutué, Planta Baja 1",Estacionam.getDireccion())   

        
    #27. Colocar telefono de estacionamiento vacio    
    def test_setTlfnVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos('')
        
     
    #28. Colocar telefono de estacionamiento no creado   
    def test_setTlfNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos(None)
        
    
    #29. Colocar telefono de estacionamiento menor a su tamanio    
    def test_setTlfnMenorTamanio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("0212555555")
        
        
    #30. Colocar te|lefono de estacionamiento solo un numero    
    def test_setTlfnSoloUno(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("4")
        
        
    #31. Colocar telefono de estacionamiento mayor a su tamanio   
    def test_setTlfnMayorTamanio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("021255555555")
        

    #32. Colocar telefono de estacionamiento con signos    
    def test_setTlfnSignos(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("0212555-555")
        
     
    #33. Colocar telefono de estacionamiento otro objeto   
    def test_setTlfnObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTelefonos("0212-555-55-55")
        
     
    #34. Mostrar el valor del Telefono obtenido
    def testgetTlfn(self):
        oEst = Estacionamiento()
        oEst.setTelefonos('02124511698')
        self.assertEqual(["02124511234",'02124511698'], oEst.getTelefonos())
        
    
    #35. Colocar telefono de estacionamiento de forma correcta   
    def test_setTlfnBuenC(self):
        oEst = Estacionamiento()
        oEst.setTelefonos("02124511234")
        
             
    #36. Prueba de none de Correo
    def testsetCorreoNone(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico(None)
    
    
    #37. Prueba de Otro tipo
    def testsetCorreoOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico(0) 
       
    
    #38. Prueba Correo vac�o
    def testsetCorreoVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("")
            
    
    #39. Prueba de Correo m�nimo
    def testsetCorreoMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setCorreoElectronico("a@a.a")

   
    #40. Prueba de Correo sin @
    def testsetCorreoSinArroba(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("a.a")
    
    
    #41. Prueba de Correo sin .
    def testsetCorreoSinPunto(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("a@a")
   
            
    #42. Prueba de correo con caracter invalido
    def testsetCorreoCaracterInvalido(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("%@ko.b")         
              
            
    #43. Prueba de solamente @ y .
    def testsetCorreoArrobaPunto(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("@.")
            
    
    #44. Prueba Extrema
    def testsetCorreoExtremo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("yyuu898_____-----hjhj2323@hjhjkjk.ko")

            
    #45. Prueba Agregar m�s de 2 correos
    def testsetMasDosCorreos(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCorreoElectronico("foo@foo.foo")
            Estacionam.setCorreoElectronico("fii@fii.fii")
            Estacionam.setCorreoElectronico("fuu@fuu.fuu")
    
    
    #46. Prueba de getCorreo
    def testgetCorreo(self):
        Estacionam = Estacionamiento()
        Estacionam.setCorreoElectronico("luisitoelmalandrito@hotmail.com")
        self.assertEqual(["luisitoelmalandrito@hotmail.com"],Estacionam.getCorreoElectronico())

            
    # 47. Colocar rif vacio   
    def test_setRifVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif('')
        
    
    # 48. Colocar rif no creado      
    def test_setRifNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif(None)
        
    
    # 49. Colocar rif con solo signos de puntuacion      
    def test_setRifSignos(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif("-.,><")
        
        
    # 50. Colocar rif otro objeto      
    def test_setRifObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif(1234)
        
        
    # 51. Colocar rif con caracteres especiales     
    def test_setRifCarEsp(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif('V-1122ñ')
            
    
    #52. Colocar rif sin J ni V de principio
    def test_setRifSinJV(self): 
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif("A1234567890")
            
        
    #53. Colocar rif sin J ni V de principio
    def test_setRifTamanioMenor(self): 
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif("J123456789")
            
            
    #54. Colocar rif sin J ni V de principio
    def test_setRifTamanioMayor(self): 
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setRif("V12345678901")
            
            
    #55. Colocar rif con J de principio
    def test_setRifJ(self): 
        oEst = Estacionamiento()
        oEst.setRif("J1234567890")
                   
            
    #56. Colocar rif con V de principio
    def test_setRifV(self): 
        oEst = Estacionamiento()
        oEst.setRif("V1234567890")
        
            
    #57. Prueba de getRif        
    def testgetRif(self):
        oEst = Estacionamiento()
        oEst.setRif("J2134308222")
        self.assertEqual("J2134308222",oEst.getRif())
        
            
    #58. Colocar rif de forma correcta     
    def test_setRifBuenC(self):
        oEst = Estacionamiento()
        oEst.setRif('J1112223334')
        
    
    #59. Colocar tarifa vacia      
    def test_setTarifaVacio(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa('')
        
    
    #60. Colocar tarifa no creada     
    def test_setTarifaNoCreado(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa(None)
            
            
    #61. Prueba de none capacidad
    def testsetCapacidad(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad(None) 
    
    
    #62. Prueba de Otro tipo
    def testsetCapacidadOtroTipo(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad("hola") 
    
    
    #63. Prueba de capacidad vac�o
    def testsetCapacidadVacio(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad("")
            
    
    #64. Prueba de Capacidad min
    def testsetCapacidadMin(self):
        Estacionam = Estacionamiento()
        Estacionam.setCapacidad("1")
   
    
    #65. Prueba de Capacidad Inv�lido simple
    def testsetCapacidadInvalido(self):
        with self.assertRaises(Exception):
            Estacionam = Estacionamiento()
            Estacionam.setCapacidad(-1)
   
    
    #66. Prueba de m�ximo Int
    def testsetCapacidadMax(self):
        Estacionam = Estacionamiento()
        Estacionam.setCapacidad(sys.maxsize)  
            

    #67. Prueba de get capacidad
    def testgetCapacidad(self):
        Estacionam = Estacionamiento()
        Estacionam.setCapacidad(54645356)
        self.assertEqual(54645356,Estacionam.getCapacidad())
        
    
    #68. Colocar tarifa vacia      
    def test_setTarifaVacia(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa("")
        
        
    #69. Colocar tarifa de otro objeto      
    def test_setTarifaObject(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa("Tarifa")
       
            
    #70. Colocar tarifa con valor cero      
    def test_setTarifaCero(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa(0)
       
            
    #71. Colocar tarifa negativa      
    def test_setTarifaNegativo(self):
        oEst = Estacionamiento()
        with self.assertRaises(Exception):
            oEst.setTarifa(-20)
       
        
    #72. Colocar tarifa de forma correcta  
    def test_setTarifaBuenC(self):
        oEst = Estacionamiento()
        oEst.setTarifa(15)
       
       
    #73. Prueba get tarifa
    def testgetTarifa(self):
        oEst = Estacionamiento()
        oEst.setTarifa(12)
        self.assertEqual(12, oEst.getTarifa())
    
             
    #74. Colocar horario iguales                
    def test_setHorarioIgual(self):
        oEst = Estacionamiento()
        oEst.setHorario("39:00am","05:00 pm" )
        
        
    #75. Colocar horario todo bien           
    def test_setHorarioBien(self):
        oEst = Estacionamiento()
        oEst.setHorario("09:00am","05:00 pm" )
        
        
    #76. Colocar horario de reserva iguales                
    def test_setHoraRIgual(self):
        oEst = Estacionamiento()
        oEst.setHorario("09:00 am","09:00 am" )
    
    
    #77. Colocar horario de reserva de forma correcta               
    def test_setHoraRBuenC(self):
        oEst = Estacionamiento()
        oEst.setHorarioReserva("09:00 am", "03:00 pm")
           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
