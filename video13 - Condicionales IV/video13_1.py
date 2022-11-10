'''
Created on 19 ago. 2019

@author: javierdt
'''

#Este es un proceso muy estricto

print("Programa de becas - 2019")
print("========================")

distancia_escuela = int(input("Ingresa la distancia a la escuela en km: "))
numero_hermanos = int(input("Ingresa el número de hermanos: "))
salario_familiar = int(input("Ingrese el salario bruto familiar: "))

print()
print("=== Estos son tus datos ===")
print("Número de hermanos", str(numero_hermanos))
print("Distancia a la escuela", str(distancia_escuela))
print("Salario familiar", salario_familiar)

print()
print("Resultado de la evualación")
if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar < 20000:
    print("TE HAS GANADO LA BECA")
else:
    print("OLVÍDATE DE LA BECA")