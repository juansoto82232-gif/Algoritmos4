'''PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Un banco necesita un sistema para gestionar la cola de clientes en espera.
Los clientes tienen diferentes tipos de atención (preferencial, normal) y
se debe poder atender, consultar y gestionar la cola.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Cliente) con los atributos necesarios
2. Diseñar la clase Lista (Cola) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos
6. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Cliente):
   - Debe almacenar: nombre, tipo de atención (preferencial/normal), 
     tiempo estimado de atención en minutos
   - Debe poder enlazarse con otro cliente

b) Clase LISTA (Cola):
   - Los clientes preferenciales van al INICIO
   - Los clientes normales van al FINAL


PUNTO 2 (1.0): AGREGAR CLIENTE - RECURSIVO
------------------------------------------
Implementa un método para agregar un cliente.
- Si es preferencial: insertar al inicio de los preferenciales
- Si es normal: insertar al final de la cola
- OBLIGATORIO usar recursividad para encontrar la posición


PUNTO 3 (1.0): TIEMPO DE ESPERA - RECURSIVO
-------------------------------------------
Implementa un método que calcule el tiempo de espera de un cliente
dado su nombre (suma de tiempos de todos los que están antes).
- OBLIGATORIO usar recursividad
- Retorna -1 si el cliente no está en la cola


PUNTO 4 (1.0): ATENDER SIGUIENTE
--------------------------------
Implementa un método que retire y retorne el primer cliente de la cola.
- Retorna None si la cola está vacía


PUNTO 5 (1.0): CONTAR POR TIPO - RECURSIVO
------------------------------------------
Implementa un método que cuente cuántos clientes hay de cada tipo.
- OBLIGATORIO usar recursividad
- Retorna una tupla (preferenciales, normales)

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════

'''# PUNTO 1a: Clase Nodo (Cliente)
#-------------------Solución------------------
class Nodo:
    def _init_(self, nombre,preferencial,normal,tiempo):
        self.nombre=nombre
        self.preferencial=preferencial
        self.normal=normal
        self.tiempo=tiempo
        self.siguiente = None  
        self.cola = None      
class lista:
    def __init__(self):
        self.cabeza=None       
    def AgregarAlFinal(self, documento, nombre):
        nodo=Nodo (documento, nombre)
        if self.cabeza==None:
            self.cabeza=nodo
        else:
            actual=self.cabeza
            while actual.siguiente != None:
                actual=actual.siguiente
            actual.siguiente=nodo 
# PUNTO 1b: Clase Lista (Cola)
#-------------------Solución------------------
class Lista:
    def _init_(self):
        self.preferencial = None  # el cliente de atención preferencial
        self.normal = None # el cliente de atención normal
# PUNTO 2: AGREGAR CLIENTE - RECURSIVO 
#-------------------Solución------------------
    def agregar(self, nombre,tiempo,Cliente):
        nuevo = Cliente(nombre, tiempo)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("No hay clientes")
            return

        while actual:
            print(f"- {actual.nombre} | {actual.tiempo}m")
            actual = actual.siguiente
#PUNTO 3: TIEMPO DE ESPERA - RECURSIVO
#-------------------Solución------------------
    def tiempo_total(self):
            return self._tiempo_total_rec(self.inicio)

        def _tiempo_total_rec(self, nodo):
            if nodo is None:
                return 0
            return nodo.tiempo + self._tiempo_total_rec(nodo.siguiente)
#PUNTO 4: ATENDER SIGUIENTE
#-------------------Solución------------------
    def retirar_cliente(self,preferencial):
        actual=self.inicio
        if actual is preferencial:
            self.preferencial()
        def retornar_cliente(self,cola):
            if cola is None:
                print("La cola esta vacía")
                return None

#PUNTO 5: CONTAR POR TIPO - RECURSIVO
#-------------------Solución------------------

# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

'''if __name__ == "__main__":
    cola = Cola()
    
    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Ana", "preferencial", 8)
    
    # Orden esperado: María, Ana, Juan, Pedro (preferenciales primero)
    cola.mostrar()
    
    # Tiempo de espera de Pedro: 5 + 8 + 10 = 23 minutos
    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))
    
    # Contar por tipo: (2 preferenciales, 2 normales)
    print("Por tipo:", cola.contar_por_tipo())
    
    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)'''

