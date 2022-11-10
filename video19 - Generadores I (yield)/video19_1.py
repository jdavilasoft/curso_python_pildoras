'''
Created on 30 ago. 2019

@author: javierdt
'''

# A continuación una funcion que devuelve numeros pares
# En el segundo ejercicio se modificafa utilizando un generador


def generaPares(limite):
    num = 1
    miLista = []
    
    while num <= limite:
        miLista.append(num * 2)
        num = num + 1
    
    return miLista


print(generaPares(10))
