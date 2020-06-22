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


#///////////////////////////////////////////////////////////// CREATES //////////////////////////////////////////////////////////////////////////


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
    create_connection(database)

    sql_tables = list()
    sql_task_table = """CREATE TABLE IF NOT EXISTS pedido (
                            id integer PRIMARY KEY,                            
                            fecha text NOT NULL,
                            cliente text NOT NULL,                             
                            monto integer 
                            );""" 
    sql_tables.append(sql_task_table) 

    sql_project_table = """ CREATE TABLE IF NOT EXISTS pizza (
                                id integer PRIMARY KEY,
                                tamano text NOT NULL,
                                jamon integer,
                                champinon integer,
                                pimenton integer,
                                dob_queso integer,
                                aceitunas integer,
                                pepperoni integer,
                                salchichon integer
                                ); """
    sql_tables.append(sql_project_table) 
    """nota: las variables con nombres de ingredientes son de tipo integer porque indican la cantidad de raciones de los mismos en la pizza"""    
                        
    """ iteración que crea las tablas """
    conn = create_connection(database)                            
    if conn is not None:
        for sql in sql_tables:
            create_table(conn, sql)
    else:
        print("Error, no se pudo crear la conexión a la base de datos")



#///////////////////////////////////////////////////////////// INSERTS //////////////////////////////////////////////////////////////////////////


""""inserts de cada tabla"""

def insert_pizza(conn, pizza):
    sql = ''' INSERT INTO pizza(tamano, jamon, champinon, pimenton, dob_queso, aceitunas, pepperoni, salchichon)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pizza)
    return cur.lastrowid

def insert_pedido(conn, pedido):
    sql = ''' INSERT INTO pedido(fecha, cliente)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pedido)
    return cur.lastrowid



#///////////////////////////////////////////////////////////// PRECIOS //////////////////////////////////////////////////////////////////////////


""""Diccionarios de precios"""
p_pizza = {'personal': 10, 'mediana': 15, 'familiar': 20} 
p_jamon = {'personal': 1.50, 'mediana': 1.75, 'familiar': 2.00} 
p_champinon = {'personal': 1.75, 'mediana': 2.05, 'familiar': 2.50}  
p_pimenton = {'personal': 1.5, 'mediana': 1.75, 'familiar': 2.00}  
p_dob_queso = {'personal': 0.80, 'mediana': 1.30, 'familiar': 1.70}  
p_aceitunas = {'personal': 1.80, 'mediana': 2.15, 'familiar': 2.60}  
p_pepperoni = {'personal': 1.25, 'mediana': 1.70, 'familiar': 1.90}  
p_salchichon = {'personal': 1.60, 'mediana': 1.85, 'familiar': 2.10}  


#///////////////////////////////////////////////////////////// SELECTS //////////////////////////////////////////////////////////////////////////


""""Buscar el ID de un pedido por su fecha """

info_pedido = list() #el primer dato de la lista debe ser el cliente y el segundo debe ser la fecha
def select_idpedido(conn, info_pedido):

    cur = conn.cursor()
    cur.execute("SELECT id FROM pedido WHERE fecha=? and cliente=?", info_pedido)
 
    rows = cur.fetchall()
 
    for row in rows:         
        p =row

    return p
"""nota: para guardar el valor del id en una variable se haría así: nombre_variable = select_idpedido(conn,pedido_prueba)[0])"""

#///////////////////////////////////////////////////////////// EJECUCIÓN //////////////////////////////////////////////////////////////////////////

"""EJECUCIONES PRINCIPALES"""

"""Ejecución del creador de tablas"""
crear_tablas()

"""
database = "pizzadb.db"
conn = create_connection(database)
cur = conn.cursor()
pedido_prueba = ('05/06/2020','Rosa Quiñones')
insert_pedido(conn, pedido_prueba)
print (select_idpedido(conn,pedido_prueba)[0])
"""


# cur.execute("SELECT * FROM sqlite_master WHERE type = 'table'")