'''
Created on 24 ago. 2019

@author: javierdt
'''

# El programa funciona igual si se elimina este import
from io import open

# Leer archivo de texto

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

frase = archivo_texto.read()

archivo_texto.close()

print(frase)
