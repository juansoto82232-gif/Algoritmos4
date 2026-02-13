def factorial(n):
    if n<=1:
       return 1
    return n * factorial(n-1)
print(factorial(5))
#Otra forma 
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado
print(factorial(5))
