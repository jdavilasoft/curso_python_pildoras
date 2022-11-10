'''
Created on 5 set. 2019

@author: javierdt
'''

import sqlite3

cnx = sqlite3.connect("firstdb")

myCursor = cnx.cursor()

# myCursor.execute("CREATE TABLE PRODUCTOS(nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

listaProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cermámica"),
    ("Camión", 20, "Juguetes")
]

myCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", listaProductos)

cnx.commit()

cnx.close()
