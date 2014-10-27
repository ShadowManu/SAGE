import unittest
from Reserva import reservarPuesto

class Test(unittest.TestCase):

   
    def testMatrizMinHoraMinT(self):
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (1,1)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento[0][0], 2, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 0, "Error al asociar elprimer puesto que consigue")
        
    def testMatrizMinHoraMaxT(self):
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (24,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento[0][23], 2, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 0, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMinTempranoF(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuesto = dict()
        tiempo = (1,1)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        estadoEstacionamientoAct = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuestoAct = dict()
        
        self.assertEqual(resultados, False, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoAct, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, False, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto, placaPuestoAct, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMinTardeF(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuesto = dict()
        tiempo = (24,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        estadoEstacionamientoAct = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuestoAct = dict()
        
        self.assertEqual(resultados, False, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoAct, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, False, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto, placaPuestoAct, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMinIntervaloTempranoF(self):
        estadoEstacionamiento = [[0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuesto = dict()
        tiempo = (1,3)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        estadoEstacionamientoAct = [[0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuestoAct = dict()
        
        self.assertEqual(resultados, False, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoAct, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, False, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto, placaPuestoAct, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMinIntervaloTardeF(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1]]
        placaPuesto = dict()
        tiempo = (20,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        estadoEstacionamientoAct = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1]]
        placaPuestoAct = dict()
        
        self.assertEqual(resultados, False, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoAct, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, False, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto, placaPuestoAct, "Error al asociar el primer puesto que consigue")
    
    def testMatrizMinHoraMultMaxT(self):
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (1,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
    
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento[0], [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 0, "Error al asociar el primer puesto que consigue")
   
    def testMatrizMaxUltimoDiaT(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (1,3)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        estadoEstacionamientoComp = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 9, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMaxPrimerDiaT(self):
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (1,3)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        estadoEstacionamientoComp = [[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 0, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMaxIntermedioDiaT(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuesto = dict()
        tiempo = (1,3)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        estadoEstacionamientoComp = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 5, "Error al asociar el primer puesto que consigue")
            
    def testMatrizMaxUltimoDiaTardeT(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (22,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        estadoEstacionamientoComp = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2]]
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 9, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMaxPrimerDiaTardeT(self):
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        placaPuesto = dict()
        tiempo = (22,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)

        estadoEstacionamientoComp = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 0, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMaxIntermedioDiaTardeT(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuesto = dict()
        tiempo = (22,24)
        placa = "CH1LL"
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        estadoEstacionamientoComp = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.assertEqual(resultados, True, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, True, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto["CH1LL"], 5, "Error al asociar el primer puesto que consigue")
        
    def testMatrizMaxF(self):
        estadoEstacionamiento = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        placaPuesto = dict()
        tiempo = (22,24)
        placa = "CH1LL"
        placaPuestoAct = placaPuesto
        estadoEstacionamientoComp = estadoEstacionamiento
        resultados = reservarPuesto(estadoEstacionamiento,tiempo,placa,placaPuesto)
        
        self.assertEqual(resultados, False, "Error al especificar que si exitia un puesto")
        self.assertEqual(estadoEstacionamiento, estadoEstacionamientoComp, "Error al actualizar la matriz de estacionamiento")
        self.assertEqual("CH1LL" in placaPuesto, False, "Error al asociar el puesto con la placa")
        self.assertEqual(placaPuesto, placaPuestoAct, "Error al asociar el primer puesto que consigue")

            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()