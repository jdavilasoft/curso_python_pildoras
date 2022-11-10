'''
Created on 24 ago. 2019

@author: javierdt
'''

# Vamos a escribir una lista de varias lineas en el archivo
archivo_texto = open("arhivo.txt", "r+", encoding="utf-8")

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
