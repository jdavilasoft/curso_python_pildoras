'''
Created on 24 ago. 2019

@author: javierdt
'''

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

# Le podemos indicar al metodo 'read'
# que lea una cantidad de caracteres determinado
print(archivo_texto.read(11))

# Luego podemos leer nuevamente y leera el resto
print(archivo_texto.read())
