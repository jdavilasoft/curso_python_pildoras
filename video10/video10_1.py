'''
Created on 16 ago. 2019

@author: javierdt
'''

# Veremmos condicionales

print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Ingrese la nota del alumno: ")


def evaluar(nota):
    valoracion = "Aprobado"
    if nota <= 10:
        valoracion = "Desaprobado"
        
    nota_alumno = 50
    print(nota_alumno)
    return valoracion


# Cualquier dato que se ingrese a traves de la función 'input()', es considerado texto
print(evaluar(int(nota_alumno)))
print(nota_alumno)
