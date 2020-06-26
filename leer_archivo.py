import os
import database_pizza as db

""" Copia el archivo en una lista donde cada elemento de la lista es una linea del archivo"""
def lectura():
    archivo = open("pedidos1.pz","r")
    
    lista_pedidos = list ()
    for linea in archivo.readlines():
        lista_pedidos.append(linea)

    archivo.close()
    """
    for i in lista_pedidos:
        print(i)
    """
    return lista_pedidos


""" calcula el id del próximo pedido a insertar"""
def calcula_id():
    database = "pizzadb1.db"
    conn = db.create_connection(database)

    cur_one = conn.cursor()
    cur_one.execute("select max(id) from pedido")
    row_one = cur_one.fetchone()
    for row in row_one:
        last_id = row

    pedidoid = last_id +1
    #print(pedidoid)
    return pedidoid



""" recorrido de la lista"""
def recorre_lista(p):
    lista_pedidos = p
    database = "pizzadb.db"
    conn = db.create_connection(database)

    for i in lista_pedidos:
        line = i
        if line == 'COMIENZO_PEDIDO':
            print(line)


""" 
- se copia el archivo .pz en una lista donde cada elemento de la lista es una fila del archivo
- buscas el indice de los Comienzo_pedido en la lista
- buscas el indice de los fin_pedido en la lista
- con eso sabes que el elemento que viene después de comienzo_pedido tiene el nombre del cliente y la fecha del pedido --> creas el pedido
- con eso también sabes que los demás elementos que vienen antes del próximo fin_pedido son pizzas --> creas las pizzas y le asignas el valor del pedido con la función calcula_id()
- Llegas a fin_pedido y todo lo que se hizo se repite hasta llegar al final de la lista.
"""

p = lectura()
recorre_lista(p)












