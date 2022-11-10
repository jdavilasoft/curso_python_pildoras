'''
Created on 24 ago. 2019

@author: javierdt
'''

archivo_texto = open("arhivo.txt", "r", encoding="utf-8")

print(archivo_texto.read())

# Python deja el cursor al final del archivo despues de leer
# Es por eso que si queremos leer una vez mas, ya no encuentra nada
print(archivo_texto.read())
