'''
Created on 24 ago. 2019

@author: javierdt
'''

# El programa funciona igual si se elimina este import
from io import open

# Crear y escribir texto en un arhivo

archivo_texto = open("arhivo.txt", "w", encoding="utf-8")

frase = "Estupendo día para estudiar: \nManipulación de archivos con Python"

archivo_texto.write(frase)

archivo_texto.close()
