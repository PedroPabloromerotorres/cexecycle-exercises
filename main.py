#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

#Ingrese num: 1
#Ingrese num: 7
#La suma es 20

num1 = int(input("Ingrese el primer número: "))

num2 = int(input("Ingrese el segundo número: "))

inicio = min(num1, num2) + 1

fin = max(num1, num2)

suma = sum(range(inicio, fin))

print(f"La suma es {suma}")