'''
Created on 14 ago. 2019

@author: javierdt
'''

# Creamos un diccionario de texto
midiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres"}

# Insertamos un elemento al final del diccionario
midiccionario["Italia"] = "Jaén"

# Imprimimos el diccionario
print(midiccionario)

# Actualizar o modificar un valor de una clave
midiccionario["Italia"] = "Roma"

# Imprimimos el diccionario
print(midiccionario)

# Eliminar un elemento del diccionario
del midiccionario["Reino Unido"]

# Imprimimos el diccionario
print(midiccionario)
