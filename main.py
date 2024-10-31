#La secuencia de Collatz de un número entero se construye de la siguiente forma:

#si el número es par, se lo divide por dos;
#si es impar, se le multiplica tres y se le suma uno;
#la sucesión termina al llegar a uno.
#La conjetura de Collatz afirma que, al partir desde cualquier número, la secuencia siempre llegará a 1. 
# A pesar de ser una afirmación a simple vista muy simple, no se ha podido demostrar si es cierta o no.

#Usando computadores, se ha verificado que la sucesión efectivamente llega a 1 partiendo desde cualquier número natural menor que 258
#.

#Desarrolle un programa que entregue la secuencia de Collatz de un número entero:

#n: 18
#18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#n: 19
#19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#n: 20
#20 10 5 16 8 4 2 1
#Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros positivos menores que el ingresado por el usuario:

#n: 20
#1 *
#2 **
#3 ********
#4 ***
#5 ******
#6 *********
#7 *****************
#8 ****
#9 ********************
#10 *******
#11 ***************
#12 **********
#13 **********
#14 ******************
#15 ******************
#16 *****
#17 *************
#18 *********************
#19 *********************
#20 ********

def collatz(n):
    """Genera la secuencia de Collatz para un número n."""
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    secuencia.append(1)  # Agregar el 1 al final
    return secuencia

# Solicitar al usuario un número
numero = int(input("n: "))
secuencia = collatz(numero)

# Mostrar la secuencia
print(" ".join(map(str, secuencia)))


def longitud_collatz(n):
    """Calcula la longitud de la secuencia de Collatz para un número n."""
    longitud = 0
    while n != 1:
        longitud += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return longitud + 1  # +1 para incluir el 1

# Solicitar al usuario un número
limite = int(input("n: "))

# Calcular y mostrar la longitud de las secuencias de Collatz
for i in range(1, limite + 1):
    longitud = longitud_collatz(i)
    print(f"{i} {'*' * longitud}")