'''
Created on 17 ago. 2019

@author: javierdt
'''

salario_presidente = int(input("Ingresa el salario del presidente: "))
salario_director = int(input("Ingresa el salario del director: "))
salario_jefearea = int(input("Ingresa el salario del jefe de área: "))
salario_administrativo = int(input("Ingresa el salario del administrativo: "))

print("Salario presidente: " + str(salario_presidente))
print("Salario presidente: " + str(salario_director))
print("Salario presidente: " + str(salario_jefearea))
print("Salario presidente: " + str(salario_administrativo))

if salario_administrativo < salario_jefearea < salario_director < salario_presidente:
    print("Todo correcto")
else:
    print("Esta empresa no está bien organizada")
