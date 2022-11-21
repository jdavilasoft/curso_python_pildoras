'''
Created on 24 ago. 2019

@author: javierdt
'''

# Con el valor 'r+' en el segundo parametro,
# le indicamos que se abra en modeo lectura/escritura 
archivo_texto = open("arhivo.txt", "r+", encoding="utf-8")

# Sobreescribimos al inicio del archivo
archivo_texto.write("Comienzo del texto")

archivo_texto.close()
