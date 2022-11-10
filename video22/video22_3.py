'''
Created on 30 ago. 2019

@author: javierdt
'''

# Podemos especificar solo la instrucción "except"
# para capturar cualquier error


def divide():
    try:
        opt1 = float(input("Ingresa un número: "))
        opt2 = float(input("Ingresa otro número: "))
        print("La división es: " + str(opt1 / opt2))
    except:
        print("Ha ocurrido un error")
    
    print("Calculo finalizado")

          
divide()
