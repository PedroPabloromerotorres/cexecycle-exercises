#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

#Ingrese num: 10
#1 2 4 8 16 32 64 128 256 512 1024

num = int(input("Ingrese un número: "))

potencias = [2**i for i in range(num + 1)]

print(" ".join(map(str, potencias)))