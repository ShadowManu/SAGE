'''
Created on 23/10/2014

@author: Jesus Adolfo Parra
@author: Edgar Valderrama
(agregar todos los demas)
'''
import unittest
import TiempoACobrar
import helpers

class Test(unittest.TestCase):

# Prueba para un cliente que nunca estaciono
    def testNoEstaciono(self):
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        placa="BAD"
        horaSalida=0
        placaPuesto={}
        placaPuesto[placa]=1
        resultado = TiempoACobrar.TiempoACobrar(estadoEstacionamiento, placa, horaSalida, placaPuesto)
        self.assertEqual(resultado[0], 0, "Error nunca no uso un puesto reservado")
        self.assertEqual(resultado[1], 0, "Error nunca ocupo un puesto reservado")
        self.assertEqual(resultado[2], 0, "Error nunca ocupo un puesto")
        
# Prueba para un cliente que estaciono todo el dia
    def testEstacionoTodoelDia(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        placa="BAD"
        horaSalida=10
        placaPuesto={}
        placaPuesto[placa]=0
        resultado = TiempoACobrar.TiempoACobrar(estadoEstacionamiento, placa, horaSalida, placaPuesto)
        helpers.placaTurno[placa]=1
        self.assertEqual(resultado[0], 0, "Error nunca no uso un puesto reservado")
        self.assertEqual(resultado[1], 0, "Error nunca ocupo un puesto reservado")
        self.assertEqual(resultado[2], 10, "Error el uso el puesto todo el dia")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()