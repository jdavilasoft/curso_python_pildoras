'''
Created on 12 ago. 2019

@author: javierdt
'''
    
# Convertir una lista en tupla
mi_lista = ["Javier", "Marimar", True, 666, "Marimar", 666]
mi_tupla = tuple(mi_lista)
print(mi_tupla)

# Verificar que un elemento exista en una tupla
print("Marimar" in mi_tupla)

# Para saber cuantas veces se encuentra un elemento en la tupla
print(mi_tupla.count(666))

# Para saber la cantidad de elementos de la tupla
print(len(mi_tupla))

