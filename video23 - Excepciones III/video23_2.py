'''
Created on 10 oct. 2022

@author: javierdt
'''

def evaluaEdad(edad):

    if edad < 0:
        raise MiPropioError("No se permite valores negativos")

    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        return "Cuidate..."
    else:
        return "RIP"

print(evaluaEdad(-5))