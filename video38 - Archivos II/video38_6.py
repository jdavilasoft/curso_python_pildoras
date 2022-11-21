'''
Created on 24 ago. 2019

@author: javierdt
'''

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

# Para omitir la primera linea y ubicarnos al final
archivo_texto.seek(len(archivo_texto.readline()))

# Leemos el texto, excepto la primera linea
print(archivo_texto.read())
