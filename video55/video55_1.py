'''
Created on 5 set. 2019

@author: javierdt
'''

import sqlite3

cnx = sqlite3.connect("firstdb")

myCursor = cnx.cursor()

# myCursor.execute("CREATE TABLE PRODUCTOS(nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

myCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

cnx.commit()

cnx.close()
