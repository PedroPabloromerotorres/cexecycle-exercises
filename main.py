#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

#Ingrese un numero: 9
#9 x 1 = 9
#9 x 2 = 18
#9 x 3 = 27
#9 x 4 = 36
#9 x 5 = 45
#9 x 6 = 54
#9 x 7 = 63
#9 x 8 = 72
#9 x 9 = 81
#9 x 10 = 90

numero = int(input("Enter a number: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")