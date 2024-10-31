#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:

#12,14,18,116,132,164,…
#en forma decimal:

#0.5,0.25,0.125,0.0625,0.03125,0.015625,…
#El programa debe mostrar tres columnas que contengan la siguiente información:

#Potencia  Fraccion  Suma
#1         0.5       0.5
#2         0.25      0.75
#3         0.125     0.875
#4         0.0625    0.9375
#...       ...       ...
#El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.

potencia = 1
fraccion = 0.5
suma = 0

print(f"{'Potencia':<10} {'Fracción':<10} {'Suma':<10}")

while fraccion > 0.000001:
    suma += fraccion
    print(f"{potencia:<10} {fraccion:<10.6f} {suma:<10.6f}")
    
    potencia += 1
    fraccion /= 2 