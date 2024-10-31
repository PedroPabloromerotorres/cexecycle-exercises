#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

#Altura: 3
#Ancho: 5

#*****
#*****
#*****
#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

#Altura: 5

#*
#**
#***
#****
#*****
#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

#Lado: 4

#   ****
#  ******
# ********
#**********
# ********
#  ******
#   ****

altura = int(input("Altura: "))

ancho = int(input("Ancho: "))

for _ in range(altura):
    
    print('*' * ancho)
