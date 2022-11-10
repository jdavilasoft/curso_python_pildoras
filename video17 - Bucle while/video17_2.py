'''
Created on 20 ago. 2019

@author: javierdt
'''

edad = int(input("Ingresa tu edad: "))

while edad <= 0:
    print("Edad no valida, intenta nuevamente")
    edad = int(input("Ingresa tu edad: "))

print("Gracias, adelante")
print("Edad del aspirante: " + str(edad))
