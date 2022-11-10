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

# A continuación solo podemos llamar a los valores que necesitemos
# Supongamos que solo necesitamos los 3 primeros

# Entre llamada y llamada, el objeto  generador, entra en un estado de pausa ("suspension")

print(next(devuelvePares))

print("Aquí podrían ir otras instrucciones")

print(next(devuelvePares))

print("Aquí podrían ir otras instrucciones")

print(next(devuelvePares))
