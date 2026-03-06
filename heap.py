#código para organizar números en orden por orden de prioridad

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
#otra forma
#---------------------------------------------
'''
import heapq

hospital = []
turno = 0

n = int(input("Cuántos pacientes desea ingresar? "))

for i in range(n):
    nombre = input(f"Nombre del paciente {i+1}: ")
    prioridad = int(input(f"Prioridad del paciente {i+1} (1-3): "))
    
    heapq.heappush(hospital, (prioridad, turno, nombre))
    turno += 1

print("\nPacientes en orden de atención:")

while hospital:
    prioridad, turno, nombre = heapq.heappop(hospital)
    print("Paciente:", nombre)
    print("Prioridad:", prioridad)

#Un programa que me permita progrmar tareas y me diga
#cual es la siguiente tarea a realizar segun el calendario
#---------------------------------------------------
from datetime import datetime, timedelta
    
tareas = []
heapq.heapify(tareas)

hoy=datetime.now()#coge la fecha actual del computador
while True:
    linea = input("tarea:")
    if linea.lower() =="fin":
        break
    partes =linea.split(maxsplit=1)
    if len(partes) != 2:
        print("Entrada no válida. Use el formato: 'YYYY-MM-DD tarea'")
        continue
    dias = int(partes[0])
    descripcion = partes[1]
    fecha_ejecucion = hoy + timedelta(days=dias)
    heapq.heappush(tareas, (fecha_ejecucion, descripcion))
print(f"Tareas en el heap:", tareas)

print("Orden de ejecución de las tareas segun calendario: ")
while tareas:
    fecha, tarea = heapq.heappop(tareas)
    dias_restantes = (fecha - hoy).days
    print(f" en {dias_restantes} días: {tareas}")
    
print("No hay más tareas programadas.")