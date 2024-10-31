#esarolle un programa para estimar el valor de π usando la siguiente suma infinita:

#π=4(1−13+15−17+…)
#La entrada del programa debe ser un número entero n
# que indique cuántos términos de la suma se utilizará.

#n: 3
#3.466666666666667
#n: 1000
#3.140592653839794

n = int(input("n: "))

suma = 0

for k in range(n):
    
    termino = ((-1) ** k) / (2 * k + 1)

    suma += termino

pi_estimado = 4 * suma

print(pi_estimado)