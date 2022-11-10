'''
Created on 30 ago. 2019

@author: javierdt
'''

# A continuación una funcion que devuelve numeros pares utilizando un generador


def generaPares(limite):
    num = 1
    
    while num <= limite:
        yield num * 2
        num = num + 1


devuelvePares = generaPares(10)

for item in devuelvePares:
    print(item)
