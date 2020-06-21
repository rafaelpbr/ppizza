import sqlite3
from sqlite3 import Error


"""Creación de la Conexión y del cursor"""
def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    
    return conn


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""Creación de Tablas"""

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)



"""Lista de Tablas a Crear e iteración para crearlas"""

def crear_tablas():
    database = "pizzadb.db"
    create_connection("./pizzadb.db")

    sql_tables = list()
    sql_project_table = """ CREATE TABLE IF NOT EXISTS pizza (
                                id integer PRIMARY KEY,
                                tamano text NOT NULL,
                                precio real NOT NULL); """
    sql_tables.append(sql_project_table)                                

    sql_task_table = """CREATE TABLE IF NOT EXISTS cliente (
                            id integer PRIMARY KEY,
                            nombrecompleto text NOT NULL);"""
    sql_tables.append(sql_task_table)  

    sql_project_table = """ CREATE TABLE IF NOT EXISTS ingrediente (
                                id integer PRIMARY KEY,
                                nombre text NOT NULL,
                                tamano text NOT NULL,
                                precio real NOT NULL); """
    sql_tables.append(sql_project_table)                                

    sql_task_table = """CREATE TABLE IF NOT EXISTS pedido (
                            id integer PRIMARY KEY,
                            id_cliente integer NOT NULL,
                            fecha text NOT NULL,                             
                            FOREIGN KEY (id_cliente) REFERENCES cliente (id),
                            UNIQUE (id,id_cliente) 
                            );""" 
    sql_tables.append(sql_task_table) 

    sql_task_table = """CREATE TABLE IF NOT EXISTS receta (
                            id integer PRIMARY KEY,
                            id_pizza integer NOT NULL,
                            id_ingrediente integer NOT NULL,
                            id_pedido integer NOT NULL,
                            id_cliente integer NOT NULL,
                            FOREIGN KEY (id_pizza) REFERENCES pizza (id),
                            FOREIGN KEY (id_ingrediente) REFERENCES ingrediente (id),
                            FOREIGN KEY (id_pedido,id_cliente) REFERENCES pedido (id,id_cliente),
                            UNIQUE (id,id_pizza,id_ingrediente,id_pedido,id_cliente) 
                            );"""
    sql_tables.append(sql_task_table)                           

    conn = create_connection(database)                            
    if conn is not None:
        for sql in sql_tables:
            create_table(conn, sql)
    else:
        print("Error, no se pudo crear la conexión a la base de datos")


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

""""inserts de cada tabla"""

def insert_pizza(conn, pizza):
    sql = ''' INSERT INTO pizza(tamano,precio)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pizza)
    return cur.lastrowid

def insert_cliente(conn, cliente):
    sql = ''' INSERT INTO cliente(nombrecompleto)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, cliente)
    return cur.lastrowid

def insert_ingrediente(conn, ingrediente):
    sql = ''' INSERT INTO ingrediente(nombre,tamano,precio)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, ingrediente)
    return cur.lastrowid

def insert_pedido(conn, pedido):
    sql = ''' INSERT INTO pedido(id_cliente,fecha)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pedido)
    return cur.lastrowid

def insert_receta(conn, receta):
    sql = ''' INSERT INTO receta(id_pizza,id_ingrediente,id_pedido,id_cliente)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, receta)
    return cur.lastrowid


"""insercipon de datos predeterminados de las tablas pizzas e ingredientes"""
def insertar_pred():
    database = "pizzadb.db"
    conn = create_connection(database)

    with conn:
        """Datos predeterminados de las pizzas"""
        pizza1 = ('personal', 10)
        pizza2 = ('mediana', 15)
        pizza3 = ('familiar', 20)

        """inserción de los datos predeterminados de pizza"""
        insert_pizza(conn, pizza1)
        insert_pizza(conn, pizza2)
        insert_pizza(conn, pizza3)
 
        """Datos predeterminados de los ingredientes"""
        jamon1 = ('jamon', 'personal', 1.50)
        jamon2 = ('jamon', 'mediana', 1.75)
        jamon3 = ('jamon', 'familiar', 2.00)

        champiñones1 = ('champiñones', 'personal', 1.75)
        champiñones2 = ('champiñones', 'mediana', 2.05)
        champiñones3 = ('champiñones', 'familiar', 2.50)

        pimenton1 = ('pimentón', 'personal', 1.50)
        pimenton2 = ('pimentón', 'mediana', 1.75)
        pimenton3 = ('pimentón', 'familiar', 2.00)

        dobqueso1 = ('doble queso', 'personal', 0.80)
        dobqueso2 = ('doble queso', 'mediana', 1.30)
        dobqueso3 = ('doble queso', 'familiar', 1.70)

        aceitunas1 = ('aceitunas', 'personal', 1.80)
        aceitunas2 = ('aceitunas', 'mediana', 2.15)
        aceitunas3 = ('aceitunas', 'familiar', 2.60)

        peppperoni1 = ('peppperoni', 'personal', 1.25)
        peppperoni2 = ('peppperoni', 'mediana', 1.70)
        peppperoni3 = ('peppperoni', 'familiar', 1.90)

        salchichon1 = ('salchichon', 'personal', 1.60)
        salchichon2 = ('salchichon', 'mediana', 1.85)
        salchichon3 = ('salchichon', 'familiar', 2.10)

        base1 = ('margarita', 'personal', 0)
        base2 = ('margarita', 'mediana', 0)
        base3 = ('margarita', 'familiar', 0)
        
        """inserción de los datos predeterminados de ingredientes"""
        insert_ingrediente(conn, jamon1)
        insert_ingrediente(conn, jamon2)
        insert_ingrediente(conn, jamon3)
        insert_ingrediente(conn, champiñones1)
        insert_ingrediente(conn, champiñones2)
        insert_ingrediente(conn, champiñones3)
        insert_ingrediente(conn, pimenton1)
        insert_ingrediente(conn, pimenton2)
        insert_ingrediente(conn, pimenton3)
        insert_ingrediente(conn, dobqueso1)
        insert_ingrediente(conn, dobqueso2)
        insert_ingrediente(conn, dobqueso3)
        insert_ingrediente(conn, aceitunas1)
        insert_ingrediente(conn, aceitunas2)
        insert_ingrediente(conn, aceitunas3)
        insert_ingrediente(conn, peppperoni1)
        insert_ingrediente(conn, peppperoni2)
        insert_ingrediente(conn, peppperoni3)
        insert_ingrediente(conn, salchichon1)
        insert_ingrediente(conn, salchichon2)
        insert_ingrediente(conn, salchichon3)
        insert_ingrediente(conn, base1)
        insert_ingrediente(conn, base2)
        insert_ingrediente(conn, base3)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""EJECUCIONES PRINCIPALES"""

"""Ejecución del creador de tablas"""
crear_tablas()

"""Ejecución de la inserción de datos predeterminados"""
insertar_pred()