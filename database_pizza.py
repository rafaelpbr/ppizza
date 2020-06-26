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
    database = "pizzadb1.db"
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
                                id_pedido integer NOT NULL,
                                tamano text NOT NULL,
                                jamon integer,
                                champinon integer,
                                pimenton integer,
                                dob_queso integer,
                                aceitunas integer,
                                pepperoni integer,
                                salchichon integer,
                                FOREIGN KEY (id_pedido) REFERENCES pedido (id)
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
    sql = ''' INSERT INTO pizza(id_pedido,tamano, jamon, champinon, pimenton, dob_queso, aceitunas, pepperoni, salchichon)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pizza)
    return cur.lastrowid

def insert_pedido(conn, pedido):
    sql = ''' INSERT INTO pedido(fecha, cliente)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pedido)
    return cur.lastrowid



""" calcula el id del próximo pedido a insertar"""
def calcula_id(conn):
        
    cur_one = conn.cursor()
    cur_one.execute("select count(id) from pedido")
    row_one = cur_one.fetchone()
    for row in row_one:
        last_id = row 
        id_correcto =last_id -1

    #print(pedidoid)
    return id_correcto



def insertar_nuevo_pedido(fecha,cliente):
    database = "pizzadb.db"
    conn = create_connection(database)

    with conn:
        
        """Datos pedidos""" 
        pedido_datos = (fecha,cliente)
        
        """inserción de pedidos"""
        insert_pedido(conn, pedido_datos) 

    




def insertar_nueva_pizza(tamano, jamon, champinon, pimenton, dob_queso, aceitunas, pepperoni, salchichon):
    database = "pizzadb.db"
    conn = create_connection(database)

    with conn:        

        id_pedido = calcula_id(conn) 

        """Datos pizzas""" 
        pizza_datos = (id_pedido,tamano, jamon, champinon, pimenton, dob_queso, aceitunas, pepperoni, salchichon)        

        """inserción de pizzas"""
        insert_pizza(conn, pizza_datos)



#///////////////////////////////////////////////////////////// PRECIOS //////////////////////////////////////////////////////////////////////////


""""Diccionarios de precios"""
price_pizza = {'personal': 10, 'mediana': 15, 'familiar': 20} 
price_jamon = {'personal': 1.50, 'mediana': 1.75, 'familiar': 2.00} 
price_champinon = {'personal': 1.75, 'mediana': 2.05, 'familiar': 2.50}  
price_pimenton = {'personal': 1.5, 'mediana': 1.75, 'familiar': 2.00}  
price_dob_queso = {'personal': 0.80, 'mediana': 1.30, 'familiar': 1.70}  
price_aceitunas = {'personal': 1.80, 'mediana': 2.15, 'familiar': 2.60}  
price_pepperoni = {'personal': 1.25, 'mediana': 1.70, 'familiar': 1.90}  
price_salchichon = {'personal': 1.60, 'mediana': 1.85, 'familiar': 2.10}  


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



""" Mostrar todos los pedidos de la bd """
def select_all_pizzas(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM pizza")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)



""" Mostrar todos los pedidos de la bd """
def select_all_pedido(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM pedido order by fecha")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)



""" select fecha """
def select_fecha(conn):
    cur = conn.cursor()
    cur.execute("select e.fecha from pedido e, pizza i where e.id = i.id_pedido order by e.fecha")
 
    rows = cur.fetchone()
 
    for row in rows:
        print(row)

#///////////////////////////////////////////////////////////// EJECUCIÓN //////////////////////////////////////////////////////////////////////////

"""EJECUCIONES PRINCIPALES"""

"""Ejecución del creador de tablas"""
crear_tablas()


# cur.execute("SELECT * FROM sqlite_master WHERE type = 'table'")