'''
Created on 24 ago. 2019

@author: javierdt
'''

# El programa funciona igual si se elimina este import
from io import open

# Leer archivo de texto por líneas

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

lineas = archivo_texto.readlines()

archivo_texto.close()

# Mostramos toda la lista
print(lineas)

# Mostramos linea a linea
for item in lineas:
    print(item)

# Mostramos solo un linea
print(lineas[1])
