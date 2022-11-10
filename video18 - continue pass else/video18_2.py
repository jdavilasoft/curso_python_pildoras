'''
Created on 20 ago. 2019

@author: javierdt
'''

# Vamos a contar letras, sin espacios
nombre = "pildoras informaticas"
contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1
    
print(contador)

