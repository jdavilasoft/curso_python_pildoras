'''
Created on 24 ago. 2019

@author: javierdt
'''

# El programa funciona igual si se elimina este import
from io import open

# Añadir (append) texto a un archivo

archivo_texto = open("arhivo.txt", "a", encoding="utf-8")

archivo_texto.write("\nEscribo una línea mas, xd, xd, xd...")

archivo_texto.close()

