'''
Created on 5 set. 2019

@author: javierdt
'''

import sqlite3

cnx = sqlite3.connect("firstdb")

myCursor = cnx.cursor()

# myCursor.execute("CREATE TABLE PRODUCTOS(nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

myCursor.execute("SELECT * FROM PRODUCTOS") 

listaProductos = myCursor.fetchall()

for item in listaProductos:
    print("Nombre artículo: " + item[0] + " \tPrecio: " + str(item[1]))

cnx.commit()

cnx.close()