'''
Created on 19 ago. 2019

@author: javierdt
'''

# Prototipo para validar un email

contador = 0
email = input("Ingresa tu email: ")

for i in email:
    if i == "@" or i == ".":
        contador += 1

if contador == 2:
    print("Email correcto")
else:
    print("Email incorrecto")
