'''
Created on 20 ago. 2019

@author: javierdt
'''

print(" Función range ")
print("===============")
# Funciones de tipo f, a partir de python 3.6
for i in range(5):
    print(f"El valor de la variable {{i}} es igual a: {i}")

print()
print(" Otro range ")
print("============")
# A la funcion range, podemos indicar un valor inicial y un valor final 
for i in range(5, 10):
    print(f"El valor de la variable {{i}} es igual a: {i}")

print()
print(" Otro range ")
print("============")
# A la funcion range, podemos indicar un valor inicial y un valor final y el incremento
for i in range(5, 20, 2):
    print(f"El valor de la variable {{i}} es igual a: {i}")
