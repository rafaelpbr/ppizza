import sqlite3
from database_creates_inserts import *

#Calcula cuantos pedidos hay en el archivo y cual es el indice donde comienza cada pedido
class Pedido():

    def __init__ (self, archivo):
        self.archivo = archivo
        

    def numero_pedidos (self):

        x = 0
        y = []
        cont = len(self.archivo)
        for i in range(int(cont)):
            if self.archivo[0] == self.archivo[i]:
                x += 1
                y.append(i)
        return y
#Retorna el nombre de cada persona por pedido
class Personas (Pedido):

    def __init__ (self):
        super().__init__()
    
    def nombre_cliente (self):

        sacar = super().numero_pedidos()
        nombre = ""
        segundo = ""
        apellido = ""
        list_nombre = []
        list_apellido = []
        for i in sacar:
            nombre = super().self.archivo[i+1]
            for d in nombre:
                if d == " ":
                    break
                segundo = segundo + d
            list_nombre.append(segundo)
            segundo = ""
        return list_nombre    
# Guarda en una lista cuantas veces se ha pedido un tipo de pizza y cuantas veces se ha pedido un ingrediente por cada tipo de pizza
class Tipo_pizza (Pedido):

    def __init__(self, archivo):
        super().__init__(archivo)

    def p_personal (self):

        personal = 0
        champiñones = 0
        jamon = 0
        pimenton = 0
        doble_queso = 0
        aceitunas = 0
        pepperoni = 0
        salchichon = 0
        ingredientes = []
        for pizza in c:
    
            if pizza.count("personal") == 1:
        
                personal += pizza.count("personal")
                jamon += pizza.count("jam")
                pimenton += pizza.count("pimen")
                doble_queso += pizza.count ("doble queso")
                aceitunas += pizza.count("aceitunas")
                pepperoni += pizza.count("pepperoni")
                salchichon += pizza.count("salchi")
                champiñones += pizza.count("champ")

        self.personal = personal
        
    
    def get_personal (self):
        return self.personal
    
    def get_ingredientes_personal(self):
        print (f'Se pidio: {jamon} de jamon, {pimenton} de pimenton, {doble_queso} de doble queso, {aceitunas} de aceitunas {pepperoni} de peperoni, {salchichon} de salchichon y {champiñones} de champiñones, tamaño personal')

#prueba de la logica para poder realizar las clases 
f = open ("pedidos1.pz", "r")
c = f.readlines()
b = Personas(c)
print (b.numero_pedidos())
print (b.nombre_cliente())


cont = len(c)
for i in range(int(cont)):
    if c[0] == c[i]:
        x += 1
        y.append(i)
print(x)
print(y)
segundo = ""
list_nombre = []

mediana = 0
familiar = 0
champiñones = 0
jamon = 0
pimenton = 0
doble_queso = 0
aceitunas = 0
pepperoni = 0
salchichon = 0

for i in y:
    nombre =c[i+1]
    for d in nombre:
        if d == " ":
            break
        segundo = segundo + d
    list_nombre.append(segundo)
    segundo = ""


champiñones = 0
jamon = 0
pimenton = 0
doble_queso = 0
aceitunas = 0
pepperoni = 0
salchichon = 0
for pizza in c:    

    if pizza.count("mediana") == 1:
    
        mediana += pizza.count("mediana")
        jamon += pizza.count("jam")
        pimenton += pizza.count("pimen")
        doble_queso += pizza.count ("doble queso")
        aceitunas += pizza.count("aceitunas")
        pepperoni += pizza.count("pepperoni")
        salchichon += pizza.count("salchi")
        champiñones += pizza.count("champ")
print (f'Se pidio: {jamon} de jamon, {pimenton} de pimenton, {doble_queso} de doble queso, {aceitunas} de aceitunas {pepperoni} de peperoni, {salchichon} de salchichon y {champiñones} de champiñones, tamaño mediana')    

champiñones = 0
jamon = 0
pimenton = 0
doble_queso = 0
aceitunas = 0
pepperoni = 0
salchichon = 0

for pizza in c:    
    

    if pizza.count("familiar") == 1:
        
        familiar += pizza.count("familiar")
        jamon += pizza.count("jam")
        pimenton += pizza.count("pimen")
        doble_queso += pizza.count ("doble queso")
        aceitunas += pizza.count("aceitunas")
        pepperoni += pizza.count("pepperoni")
        salchichon += pizza.count("salchi")
        champiñones += pizza.count("champ")

print (f'Se pidio: {jamon} de jamon, {pimenton} de pimenton, {doble_queso} de doble queso, {aceitunas} de aceitunas {pepperoni} de peperoni, {salchichon} de salchichon y {champiñones} de champiñones, tamaño familiar')

print ("Pidió ", personal, " personal ", "\nPidió ", mediana, " mediana ", "\nPidió ", familiar, " familiar")

print(list_nombre)
        





#Creación del archivo resumen con los datos recolectados del archivo pedidos
"""
#Esta Clase recibe de la base de datos las entidades personal, mediana y familiar y 
# calcula por cada una de ellas el numero de pedidos y el monto total


class Clientes ():
    
    def __init__(self, tipo ):
        self.tipo = tipo
    
    def cont_personal (self):
              
              count = self.tipo.count('personal')
              monto = count*10
              return count, monto
    
    def cont_mediana (self):
              
              count = self.tipo.count('mediana')
              monto = count*15
              return count, monto
    
    def cont_familiar (self):
              
              count = self.tipo.count('familiar')
              monto = count*20
              return count, monto

#Esta Clase recibe de la base de datos la entidad ingredientes la cual tiene la columna par para el ingrediente y el tipo de pizza 
# calcula por ingrediente el monto 

class Ingredientes ():

    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
    
    def calculadora (self,):

        unidades = self.ingredientes.count()

# hay que ver que es lo que se actualiza

#quiero hacer una prueba de conflictos en commit
from database_creates_inserts import *
import sqlite3

database = "./__pycache__/pizzadb.db"
conn = create_connection(database)

def select_all(conn, entity):
    sql = "SELECT * FROM " + entity
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    return rows

def select_by_entity_field(conn, entity, field, value):
    sql = "SELECT * FROM " + entity + " WHERE " + field + "=?"
    cur = conn.cursor()
    cur.execute(sql, (value,))

    rows = cur.fetchall()
    return rows

prueba = select_all(conn, "pizza")
print (prueba)
print("\n".join([str(g[2]) for g in prueba ]))"""