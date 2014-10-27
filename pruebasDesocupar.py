'''
Created on 23/10/2014

@author: Cristian Medina
'''
import unittest
from Desocupar import desocuparPuesto
from helpers import placaTurno

class Test(unittest.TestCase):


    def testDictVacio(self):
        placaPuesto = dict()
        placaPuestoComp = placaPuesto
        
        resultados = desocuparPuesto(None, "CH1LL", 2, placaPuesto)
        
        self.assertEqual(resultados, None, "Error al indicar el puesto")        
        self.assertEqual(placaPuesto, placaPuestoComp, "Error al actualizar diccionario placaPuesto")
    
    def testDictUnElementoT(self):
        placaPuesto = {'CH1LL':1}

        resultados = desocuparPuesto(None, "CH1LL", 2, placaPuesto)
        
        self.assertEqual(resultados, 1, "Error al indicar el puesto")
        self.assertEqual(placaPuesto, dict(), "Error al actualizar diccionario placaPuesto")
    
    def testDictMultElemT(self):
        placaPuesto = {'CH1LL':1,'C00L':2,"R3L4X":3,"CH1LL4X":4,"C4LM":5,"345Y":6}

        resultados = desocuparPuesto(None, "CH1LL", 2, placaPuesto)
        
        self.assertEqual(resultados, 1, "Error al indicar el puesto")
        self.assertEqual('CH1LL' in placaPuesto, False, "Error al actualizar diccionario placaPuesto")
    
    def testDictMultElemF(self):
        placaPuesto = {'C00L':2,"R3L4X":3,"CH1LL4X":4,"C4LM":5,"345Y":6}
        placaPuestoComp = placaPuesto
        placaTurnoComp = placaTurno
        
        resultados = desocuparPuesto(None, "CH1LL", 2, placaPuesto)
        
        self.assertEqual(resultados, None, "Error al indicar el puesto")
        self.assertEqual(placaPuesto, placaPuestoComp, "Error al actualizar diccionario placaPuesto")
    
    def testDictUnElementoF(self):
        placaPuesto = {'C00L':2}
        placaPuestoComp = placaPuesto
        
        resultados = desocuparPuesto(None, "CH1LL", 2, placaPuesto)
        
        self.assertEqual(resultados, None, "Error al indicar el puesto")   
        self.assertEqual(placaPuesto, placaPuestoComp, "Error al actualizar diccionario placaPuesto")
    
    def testHoraSobrepasadaF(self):
        placaPuesto = {'CH1LL':1}
        placaPuestoComp = placaPuesto
        
        resultados = desocuparPuesto(None, "CH1LL", 25, placaPuesto)
        
        self.assertEqual(resultados, None, "Error al indicar el puesto")   
        self.assertEqual(placaPuesto, placaPuestoComp, "Error al actualizar diccionario placaPuesto")
        
    def testHoraSubpasaF(self):
        placaPuesto = {'CH1LL':1}
        placaPuestoComp = placaPuesto
        
        resultados = desocuparPuesto(None, "CH1LL", 0, placaPuesto)
        
        self.assertEqual(resultados, None, "Error al indicar el puesto")   
        self.assertEqual(placaPuesto, placaPuestoComp, "Error al actualizar diccionario placaPuesto")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()