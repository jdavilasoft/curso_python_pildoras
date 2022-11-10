'''
Created on 30 ago. 2019

@author: javierdt
'''

# Excepciones
# Aquí se controla error en la función: divide


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operación erronea"


opt1 = int(input("Ingresa un número: "))
opt2 = int(input("Ingresa otro número: "))

operacion = input("Que operacion desea realizar (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(opt1, opt2))
elif operacion == "resta":
    print(resta(opt1, opt2))
elif operacion == "multiplica":
    print(multiplica(opt1, opt2))
elif operacion == "divide":
    print(divide(opt1, opt2))
else:
    print("Operacion no contemplada")

print("Operación terminada...")
