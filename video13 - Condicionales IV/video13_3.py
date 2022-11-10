'''
Created on 19 ago. 2019

@author: javierdt
'''

print("Asignaturas optativas año 2019")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Has elegido: " + asignatura.upper())
else:
    print("NO has escogido una asignatura")
