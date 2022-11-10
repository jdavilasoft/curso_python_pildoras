'''
Created on 10 ago. 2019

@author: javierdt
'''

# Creamos una lista y sus elementos
listaNombres = ["Javier", "Teresa", "Luis", "Fredesvinda", "Jorge", "Roberta"]

# Imprimimos un elemento de la lista, indicando el indice
# Los elementos empiezan desde el indice (0)
print(listaNombres[0])
print(listaNombres[1])

print(listaNombres)  # Imprime toda la lista
print(listaNombres[:])  # Imprime toda la lista

# Se puede indicar un indice negativo
# Python, toma los elementos del final hacia adelante
print(listaNombres[-2])
print(listaNombres[-4])

# ***** SUBLISTAS *****

# Podemos obtener una "sublista", "porción" o "lista intermedia"
# Se indica dos indices: desde donde empieza y donde termina
# El primer indice es inclusivo: Se incluye en la sublista
# El segundo indice es exclusivo: No se incluye en la sublista
print(listaNombres[2:3])

# Si el primer indice es 0 (El primer elemento), este se puede omitir
print(listaNombres[:2])

# Tambien se puede omitir segundo parametro para que muestre hasta el último elemento
print(listaNombres[3:])

# ***** SUBLISTAS *****

# Esta linea muestra error
print(listaNombres[7])
