'''
Created on 24 ago. 2019

@author: javierdt
'''

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

# Para ubicarnos en el medio del texto del archivo
archivo_texto.seek(len(archivo_texto.read()) / 2)

# Leemos solo la mitad del texto
print(archivo_texto.read())
