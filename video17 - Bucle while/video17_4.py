'''
Created on 20 ago. 2019

@author: javierdt
'''

import math

print("Programa de raiz cuadrada")
numero = int(input("Ingresa un número: "))

intentos = 1

while numero < 0:
    print("No se puede calcular la raiz de un número negativo")
    
    if intentos == 3:
        print("Solo tienes tres intentos")
        break
    
    numero = int(input("Ingresa un número: "))
    
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de: " + str(numero) + " es " + str(solucion))
