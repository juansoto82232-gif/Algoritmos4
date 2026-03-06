"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 3: CONVERSIÓN INFIJA A POSTFIJA
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

Algoritmo Shunting Yard (Dijkstra, 1961)

Convierte expresiones de notación infija a postfija usando:
- Una cola de salida (el resultado)
- Una pila de operadores

Reglas:
1. Número → va directo a la salida
2. Operador → según precedencia, puede ir a pila o mover otros a salida
3. '(' → va a la pila
4. ')' → pop hasta encontrar '('
5. Al final → vaciar pila a salida
"""

from ejemplo_01_pila import Pila


def infija_a_postfija(expresion):
    """
    Convierte una expresión infija a notación postfija.
    
    Args:
        expresion: String con expresión infija (tokens separados por espacios)
    
    Returns:
        String con expresión en notación postfija
    """
    '''
    # Precedencia de operadores (mayor número = mayor precedencia)
    precedencia = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    
    
    salida = []
    pila = Pila()
    
    # Preparar tokens (separar paréntesis)
    expresion = expresion.replace('(', ' ( ').replace(')', ' ) ')
    tokens = expresion.split()
    
    print(f"\n📝 Convirtiendo: {' '.join(tokens)}")
    print("-" * 50)
    
    for token in tokens:
        if token.lstrip('-').replace('.', '').isdigit():
            # Es un número
            salida.append(token)
            print(f"   '{token}' (número) → salida")
        
        elif token == '(':
            pila.push(token)
            print(f"   '{token}' → pila")
        
        elif token == ')':
            # Pop hasta encontrar '('
            while not pila.esta_vacia() and pila.peek() != '(':
                salida.append(pila.pop())
            if not pila.esta_vacia():
                pila.pop()  # Quitar el '('
            print(f"   '{token}' → pop hasta '('")
        
        elif token in precedencia:
            # Es un operador
            while (not pila.esta_vacia() and 
                   pila.peek() != '(' and
                   pila.peek() in precedencia and
                   precedencia[pila.peek()] >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
            print(f"   '{token}' (operador) → pila")
        
        print(f"      Salida: {salida}")
        print(f"      Pila: {pila}")
    
    # Vaciar la pila
    print("\n   Vaciando pila...")
    while not pila.esta_vacia():
        salida.append(pila.pop())
    
    resultado = ' '.join(salida)
    print(f"      Resultado: {resultado}")
    
    return resultado


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("   CONVERSIÓN INFIJA → POSTFIJA (Shunting Yard)")
    print("=" * 60)
    
    expresiones = [
        "3 + 4",
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "3 + 4 * 2 - 1",
        "( 1 + 2 ) * ( 3 + 4 )",
        "2 ** 3 ** 2",  # Asociatividad derecha: 2^(3^2) = 512
        "10 - 5 - 2",   # Asociatividad izquierda: (10-5)-2 = 3
    ]
    
    print("\n📊 Tabla de conversiones:")
    print("-" * 60)
    print(f"{'Infija':<25} {'Postfija':<25}")
    print("-" * 60)
    
    for expr in expresiones:
        postfija = infija_a_postfija(expr)
        print(f"\n{'='*60}")
        print(f"✅ {expr:<25} → {postfija:<25}")
'''        