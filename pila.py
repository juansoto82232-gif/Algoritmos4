#crear pila con nodos
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
def esta_vacia (self):
    return self.tope is None

def push(self,dato):
    self.tope=nuevo
    self.tamaño=1
def pop(self):
    if self.esta_vacia():
        return None
    dato=self.tope.dato
    self.tope=self.tope.siguiente
    self.tamaño-=1
    return dato
def peek(self):
    if self.esta_vacia():
        return None
    return self.tope.dato