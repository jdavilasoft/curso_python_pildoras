'''
Created on 10 ago. 2019

@author: javierdt
'''

# Creamos una lista y sus elementos
lista = ["Javier", 5, True, 66.66, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Quita un elemento de la lista
# Si el elemento se repite, quita el primero que encuentra
lista.remove("Javier")
lista.remove(True)

# Elimina el ultimo elemento de una lista
lista.pop()

print(lista)
