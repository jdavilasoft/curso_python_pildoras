'''
Created on 30 ago. 2019

@author: javierdt
'''

# Podemos especificar "finally", para hacer operaciones que se 
# van a ejecutar, sin importar si haya o no ocurrido un error


def divide():
    try:
        opt1 = float(input("Ingresa un número: "))
        opt2 = float(input("Ingresa otro número: "))
        print("La división es: " + str(opt1 / opt2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Calculo finalizado")          


divide()
