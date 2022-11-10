'''
Created on 24 ago. 2019

@author: javierdt
'''

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

print(archivo_texto.read())

# Nos ubicamos al inicio del archivo
archivo_texto.seek(0)

print(archivo_texto.read())
