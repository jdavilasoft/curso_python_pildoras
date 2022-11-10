'''
Created on 10 ago. 2019

@author: javierdt
'''

# Creamos una lista y sus elementos
listaNombres = ["Javier", "Teresa", "Luis"]

# Añadir un elemento al final de la lista
listaNombres.append("Fredesvinda")

# Inserta un elemento, en una posicion determinada
# Se indica el indice, donde se va a ubicar el elemento.
listaNombres.insert(2, "Jorge")

# Añadir varios elementos
# Se concatena otra lista
listaNombres.extend(["Roberta", "Luis"])

# Para saber el indice de un elemento, se indica el valor del elemento
# Si el elemento se repite en la lista, devuelve el primero que encuentra
print("Luis tiene el indice: ", listaNombres.index("Luis"))

# Para saber si un elemento está en la lista
print("Pepe" in listaNombres)
print("Javier" in listaNombres)

print(listaNombres)
