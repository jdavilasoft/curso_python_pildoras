'''
Created on 16 ago. 2019

@author: javierdt
'''

# Uso de la clausula 'elif'
print("Verificación de acceso")

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 120:
    print("Edad incorrecta")
else:
    print("Bienvendido")
    
print("Programa finalizado")
