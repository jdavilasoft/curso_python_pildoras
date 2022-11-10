'''
Created on 30 ago. 2019

@author: javierdt
'''

# Cuando al argumento de una función le pongammos un *
# le estamos diciendo que va a recibir un numero
# indeterminado de elementos en forma de tupla


def devuelveCiudades(*ciudades):
    for item in ciudades:
        for subItem in item:
            yield from subItem


ciudadesDevueltas = devuelveCiudades("madrid", "barcelaona", "bilbao", "valencia")

# Devolvemos el primer elemento
print(next(ciudadesDevueltas))

# Devolvemos el segundo elemento
print(next(ciudadesDevueltas))