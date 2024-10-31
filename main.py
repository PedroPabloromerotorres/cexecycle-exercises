#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:

#e=10!+11!+12!+13!+14!+…
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

#Recuerde que el factorial n! es el producto de los números de 1 a n.

def factorial(n):
    """Calcula el factorial de n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = 10  
suma = 0
diferencia = float('inf')

while diferencia >= 0.0001:

    term = factorial(n)
    
    suma += term
    n += 1
    
    if n > 11:  
        diferencia = abs(term - factorial(n - 1))

print(f"Valor aproximado de e: {suma}")