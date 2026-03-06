#código para organizar números en orden por orden de prioridad
'''
datos = [5, 3, 8, 1, 2, 9, 4]
import heapq
from sys import _debugmallocstats
heapq.heapify(datos)
print("Heap:",datos)

heapq.heappush(datos,6)
print("Heap después de agregar 6:",datos)

minimo = heapq.heappop(datos)
print("Elemento mínimo extraídos:",minimo)
print("Heap después de extraer el mínimo",datos)

datos2 = [(2, 'A'),(1, 'B'),(3, 'C'),(2, 'B')]
heapq.heapify(datos2)
print("Heap con tuplas:", datos2)
'''

#programa para un hospital
#Cada paciente tiene prioridad de 1 a 3, 1 es la más importante 
#Las personas del hospital deben saber quien es el siguiente en atender
#e inidcar su nombre y su prioridad
#---------------------------------
'''
class Paciente:
    def __init__(self, nombre, prioridad):
        self.nombre= nombre
        self.prioridad= prioridad
    
    def __lt__(self, otro):
        return self.prioridad < otro.prioridad
class Hospital:
    def __init__(self):
        self.pacientes= []
    
    def agregar_paciente(self, paciente):
        heapq.heappush(self.pacientes, paciente)
    
    def siguiente_paciente(self):
        if not self.pacientes:
            return None
        return heapq.heappop(self.pacientes)
hospital= Hospital()
#debo agrgar yo los nombres y prioridades de los pacientes para probar el programa
hospital.agregar_paciente(Paciente("Juan", 2))
hospital.agregar_paciente(Paciente("Maria", 1)) 
hospital.agregar_paciente(Paciente("Pedro", 3))
hospital.agregar_paciente(Paciente("Juan", 1))
siguiente= hospital.siguiente_paciente()
print(f"Siguiente paciente a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")
siguiente= hospital.siguiente_paciente()
print(f"Siguiente paciente a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")
'''
