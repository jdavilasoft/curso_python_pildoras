'''
Created on 20 ago. 2019

@author: javierdt
'''

# Para conocer que con el bucle 'while', tambien se puede utilizar la instruccion 'else'
email = input("Ingresa tu email: ")
for i in email:
    if i == "@":
        arroba = True
        break

else:
    arroba = False

print(arroba)
