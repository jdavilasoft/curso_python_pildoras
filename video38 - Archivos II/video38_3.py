'''
Created on 24 ago. 2019

@author: javierdt
'''

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

# Le indicamos que lea a partir del caracter 11 en adelante
# Los 11 primero caracteres no los lee
archivo_texto.seek(11)

print(archivo_texto.read())
