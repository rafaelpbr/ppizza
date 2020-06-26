import sqlite3
from sqlite3 import Error
import database_pizza as db


"""inserción de datos predeterminados de las tablas pizzas e ingredientes"""
def insertar_pruebas():
    database = "pizzadb.db"
    conn = db.create_connection(database)

    with conn:
        
        """Datos pedidos""" # (fecha, cliente)
        pedido1 = ('05/06/2020','Rosa Quiñones')
        pedido2 = ('06/06/2020','Luis Gómez')
        pedido3 = ('06/06/2020','Carlos Valderrama')
        pedido4 = ('06/06/2020','María Valdéz')
        pedido5 = ('06/06/2020','Rosa Quiñones')
        pedido6 = ('06/06/2020','Carmen Sarmiento')
        pedido7 = ('05/06/2020','Alberto Sanchéz')

        """inserción de pedidos"""
        db.insert_pedido(conn, pedido1)
        db.insert_pedido(conn, pedido2)
        db.insert_pedido(conn, pedido3)
        db.insert_pedido(conn, pedido4)
        db.insert_pedido(conn, pedido5)
        db.insert_pedido(conn, pedido6)
        db.insert_pedido(conn, pedido7)

        """Datos pizzas""" # (id_pedido,tamano, jamon, champinon, pimenton, dob_queso, aceitunas, pepperoni, salchichon)
        pizza1 = (1,'personal',0,0,0,0,0,0,0)
        pizza2 = (2,'personal',0,1,0,0,0,0,0)
        pizza3 = (3,'mediana',1,1,1,0,0,0,0)
        pizza4 = (4,'mediana',1,1,1,0,0,0,0)
        pizza5 = (4,'familiar',0,0,0,1,1,1,0)
        pizza6 = (4,'familiar',0,1,1,0,1,0,0)
        pizza7 = (5,'personal',1,0,0,1,0,0,0)
        pizza8 = (6,'familiar',2,0,0,0,0,1,1)
        pizza9 = (7,'personal',0,0,0,0,0,0,0)

        """inserción de pizzas"""
        db.insert_pizza(conn, pizza1)
        db.insert_pizza(conn, pizza2)
        db.insert_pizza(conn, pizza3)
        db.insert_pizza(conn, pizza4)
        db.insert_pizza(conn, pizza5)
        db.insert_pizza(conn, pizza6)
        db.insert_pizza(conn, pizza7)
        db.insert_pizza(conn, pizza8)
        db.insert_pizza(conn, pizza9)

 
        

"""Ejecución de la inserción de datos de prueba"""
#insertar_pruebas()
db.insertar_nuevo_pedido('12/06/2020','Angel Hidalgo')




        

















