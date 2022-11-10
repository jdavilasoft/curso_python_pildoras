'''
Created on 20 ago. 2019

@author: javierdt
'''

valido = False
email = input("Ingresa tu email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")
