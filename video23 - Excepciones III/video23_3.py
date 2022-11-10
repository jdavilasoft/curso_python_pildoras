'''
Created on 10 oct. 2022

@author: javierdt
'''

import math

def calculaRaiz(num):
    if num<0:
        raise ValueError("Numero no puede ser negativo")
    else:
        return math.sqrt(num)

opt = int(input("Ingresa un numero: "))

try:
    print(calculaRaiz(opt))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo) 

print('Progrma terminado')