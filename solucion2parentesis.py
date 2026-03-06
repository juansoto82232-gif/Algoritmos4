"""
═══════════════════════════════════════════════════════════════════════════════
SOLUCIÓN EJERCICIO 2: VERIFICADOR DE PARÉNTESIS BALANCEADOS
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
    
    def pop(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato


def parentesis_balanceados(expresion):
    """
    Verifica si los paréntesis, corchetes y llaves están balanceados.
    """
    '''
    pila = Pila()
    
    # Mapeo de cierre a apertura
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    aperturas = set(pares.values())  # {'(', '[', '{'}
    cierres = set(pares.keys())      # {')', ']', '}'}
    
    for caracter in expresion:
        if caracter in aperturas:
            # Es un símbolo de apertura → push
            pila.push(caracter)
        elif caracter in cierres:
            # Es un símbolo de cierre → verificar
            if pila.esta_vacia():
                return False  # Cierre sin apertura
            
            tope = pila.pop()
            if tope != pares[caracter]:
                return False  # No coinciden
    
    # La pila debe estar vacía al final
    return pila.esta_vacia()


def verificar_con_detalle(expresion):
    """
    Versión extendida que retorna información detallada del error.
    """
    pila = Pila()  # Guardará tuplas (símbolo, posición)
    
    pares = {')': '(', ']': '[', '}': '{'}
    nombres = {'(': 'paréntesis', '[': 'corchete', '{': 'llave',
               ')': 'paréntesis', ']': 'corchete', '}': 'llave'}
    
    aperturas = set(pares.values())
    cierres = set(pares.keys())
    
    for i, caracter in enumerate(expresion):
        if caracter in aperturas:
            pila.push((caracter, i))
        elif caracter in cierres:
            if pila.esta_vacia():
                return (False, f"Error en posición {i}: '{caracter}' sin {nombres[caracter]} de apertura")
            
            tope, pos_apertura = pila.pop()
            esperado = pares[caracter]
            
            if tope != esperado:
                return (False, f"Error en posición {i}: se esperaba cierre para '{tope}' pero se encontró '{caracter}'")
    
    if not pila.esta_vacia():
        simbolo, pos = pila.pop()
        return (False, f"Error: falta cerrar '{simbolo}' abierto en posición {pos}")
    
    return (True, "Expresión válida")


# ═══════════════════════════════════════════════════════════════════════════════
# PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("   VERIFICADOR DE PARÉNTESIS (SOLUCIÓN)")
    print("=" * 60)
    
    casos_prueba = [
        ("(a + b)", True),
        ("[(a + b) * c]", True),
        ("{[()]}", True),
        ("((()))", True),
        ("", True),
        ("sin paréntesis", True),
        ("(a + b]", False),
        ("((a + b)", False),
        ("a + b)", False),
        ("{[(])}", False),
        ("([)]", False),
    ]
    
    print("\n📊 Resultados función básica:")
    print("-" * 60)
    
    todos_correctos = True
    for expresion, esperado in casos_prueba:
        resultado = parentesis_balanceados(expresion)
        correcto = resultado == esperado
        todos_correctos = todos_correctos and correcto
        estado = "✅" if correcto else "❌"
        expr_mostrar = expresion if expresion else "(vacío)"
        print(f"{estado} '{expr_mostrar}' → {resultado}")
    
    print(f"\n{'✅ Todas las pruebas pasaron' if todos_correctos else '❌ Algunas pruebas fallaron'}")
    
    print("\n" + "=" * 60)
    print("   PRUEBAS CON DETALLE DE ERROR")
    print("=" * 60)
    
    casos_error = [
        "(a + b)",
        "(a + b]",
        "((a + b)",
        "a + b)",
        "{[(])}",
    ]
    
    for expr in casos_error:
        valido, mensaje = verificar_con_detalle(expr)
        estado = "✅" if valido else "❌"
        print(f"\n{estado} '{expr}'")
        print(f"   {mensaje}")
'''        