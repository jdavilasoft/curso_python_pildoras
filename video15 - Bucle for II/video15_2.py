'''
Created on 19 ago. 2019

@author: javierdt
'''

email = False

for i in "jdavila.soft@gmail.com":
    if i == "@":
        email = True

if email == True:
    print("Email es correcto")
else:
    print("El email es incorrecto")
