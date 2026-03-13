# Clase 19/02/2026

 #-------------- Funcion --------------

#  def funcion (a,b):
#  	if b == 0:
#  		return 1
#  	return a * funcion(a,b-1)
#  print(funcion(2,10))

#  #-------------- Funcion mejorada --------------

#  def funcion (a,b):
#  	if b == 0:
#  		return 1
#  	if b % 2 == 0:
#  		mitad = funcion(a, b//2)
#  		return mitad * mitad
#  	else:
#  		return funcion(a,b-1)
#  print(funcion(2,10))

#  #------------- Palíndromo --------------

#  def es_palindromo_invertir(texto):
#      limpio = texto.replace(" ", "").lower()
#      invertido = limpio[::-1]
#      return limpio == invertido
#  print(es_palindromo_invertir("Anita lava la tina")) 

#  #------------- Palíndromo --------------

#  def es_palindromo(palabra):
#      palabra = palabra.lower()
#      inicio = 0
#      fin = len(palabra) - 1
#      while inicio < fin:
#          if palabra[inicio] != palabra[fin]:
#              return False
#          inicio += 1
#          fin -= 1
#      return True
#  print(es_palindromo("Anitalavalatina"))

#  #------------- Palíndromo --------------

#  def es_palindromo(texto):
#      limpio = texto.replace(" ", "").lower()
#      izq = 0
#      der = len(limpio) - 1
#      while izq < der:
#          if limpio[izq] != limpio[der]:
#              return False
#          izq += 1
#          der -= 1
#      return True

#  print(es_palindromo("Anitalavalatina"))

#  #------------- Palíndromo recursivo --------------

#  def es_palindromo_recursivo(palabra):   
#      palabra = palabra.lower()
#      if len(palabra) <= 1:
#          return True
    
#      if palabra[0] == palabra[-1]:
#          return es_palindromo_recursivo(palabra[1:-1])
#      else:
#          return False
    
#  print(es_palindromo_recursivo("Anitalavalatina"))

#  #------------ Palindromo a n --------------

#  def es_palindromo_n(palabra, inicio, fin):
#      if inicio >= fin: # caso base
#          return True 
#      if palabra[inicio] != palabra[fin]:
#          return False
#      return es_palindromo_n(palabra, inicio + 1, fin - 1)

  #------------ Recursividad en listas --------------
# class lista:
#     def __init__(self,dato):
#         self.cabeza=None
#     ##def sumar(self, nodo=None):

#     def agregar(self):
#         nuevo=Nodo(dato)
#         if not self.cabeza:
#             self.cabeza=nuevo
#         else:
#             actual=self.cabeza
#             while actual.siguiente !=None:
#                 actual=actual.siguiente
#             actual.siguiente=nuevo
#     def buscar(self,nodo=None,dato,primera_llamada=True):
#         if primera_llamada:
#             nodo=self.cabeza
#         if nodo is None:
#             return False
#         if nodo.dato==dato:
#             return True
#         return buscar(nodo.siguiente,dato,False) 
#-----------------Suma-------------------------------
#     def suma_digito(n):
#         if n==0:
#             return 0
#         else:
#             return (n%10)+suma_digito(n//10)
#     print(suma_digito(15033))  
# --------------------Busquedad binaria--------------
#   def busquedad_binaria(lista,num,inicio,fin):
#       if lista[medio]==num:
#           return medio
#       elif num<lista[medio]:
#           return busquedad_binaria(lista,num,inicio,fin):
#           else:


#---------------permutaciones-------------
#  def permutaciones(lista):

#     if len(lista) <=1:

#          return lista
#     resultado= []

#     for i in range(len(lista)):

#         elemento=lista[i]

#         resto =lista[:i]+lista[i+1:]

#         for perm in permutaciones(resto):
#             resultado.append([elemento]+perm)
                 
#     return resultado
#-----------------Recursión de cola---------------
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1) # Operación DESPUÉS de la llamada
#     # Recursión de cola (el resultado se pasa como parámetro)
# def factorial_tail(n, acumulador=1): 
#     if n <= 1:
#         return acumulador
#     return factorial_tail(n - 1, n * acumulador) # Nada después

#     # Nota: Python NO optimiza tail recursion
#     # Pero otros lenguajes (Scheme, Scala) sí lo hacen
# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# def fibonacci_tail(n,actual=0, siguiente=1):
#     if n == 0:
#         return actual
#     return fibonacci_tail(n-1, siguiente, siguiente + actual)
#------------------suma lista----------------
def suma_lista(lista):
    if len(lista)==0:
        return 0
    return lista[0]+suma_lista(lista[1:])
#----------------------mejora-----------------------
def suma_lista(lista, acumulador=0):
    if len(lista)==0:
        return acumulador  
    return suma_lista(lista[1:],) 
#---------------------potencia----------------
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp -1)  
#------------------mejora-------------------
def potencia_tail(base, exp, acumulador= 1):
    if exp == 0:
        return acumulador
    return potencia_tail(base, exp -1, base * acumulador)         


           


                        