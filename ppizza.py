import sqlite3
from database_creates_inserts import *

#Calcula cuantos pedidos hay en el archivo y cual es el indice donde comienza cada pedido
#Retorna el nombre de cada persona por pedido
class Cliente ():

    def __init__ (self, archivo):
        self.archivo = archivo
    
    def datos_cliente (self):

        y = []
        cont = len(self.archivo)
        for i in range(int(cont)):
            if self.archivo[0] == self.archivo[i]:
                y.append(i+1)
        sacar = y
        linea = ""
        nombre = ""
        fecha = ""
        list_nombre = []
        list_fecha = []
        for i in sacar:
            linea = self.archivo[i]
            indice = linea.find(";")
            ultimo = len(linea)
            nombre = linea[:int(indice)]
            fecha = linea [int(indice):int(ultimo)-1]
            list_nombre.append(nombre)
            list_fecha.append(fecha)
        print (list_nombre, "\n", list_fecha)
# Guarda en una lista cuantas veces se ha pedido un tipo de pizza y cuantas veces se ha pedido un ingrediente por cada tipo de pizza

class Tipo_pizza ():

    def __init__(self, archivo):
        self.archivo = archivo

    def p_personal (self):

        personal = 0
        champiñones = 0
        jamon = 0
        pimenton = 0
        doble_queso = 0
        aceitunas = 0
        pepperoni = 0
        salchichon = 0
        ingredientesp = []
        
        for pizza in self.archivo:
    
            if pizza.count("personal") == 1:
        
                personal += pizza.count("personal")
                jamon += pizza.count("jam")
                pimenton += pizza.count("pimen")
                doble_queso += pizza.count ("doble queso")
                aceitunas += pizza.count("aceitunas")
                pepperoni += pizza.count("pepperoni")
                salchichon += pizza.count("salchi")
                champiñones += pizza.count("champ")
                ingredientesp.append(personal)
                ingredientesp.append(jamon)
                ingredientesp.append(pimenton)
                ingredientesp.append(doble_queso)
                ingredientesp.append(aceitunas)
                ingredientesp.append(pepperoni)
                ingredientesp.append(salchichon)
                ingredientesp.append(champiñones)
                print(ingredientesp)
                ingredientesp = []
                personal = 0
                champiñones = 0
                jamon = 0
                pimenton = 0
                doble_queso = 0
                aceitunas = 0
                pepperoni = 0
                salchichon = 0

    def p_mediana (self):

        mediana = 0
        champiñones = 0
        jamon = 0
        pimenton = 0
        doble_queso = 0
        aceitunas = 0
        pepperoni = 0
        salchichon = 0
        ingredientesm = []
        
        for pizza in self.archivo:
    
            if pizza.count("mediana") == 1:
        
                mediana += pizza.count("mediana")
                jamon += pizza.count("jam")
                pimenton += pizza.count("pimen")
                doble_queso += pizza.count ("doble queso")
                aceitunas += pizza.count("aceitunas")
                pepperoni += pizza.count("pepperoni")
                salchichon += pizza.count("salchi")
                champiñones += pizza.count("champ")
                ingredientesm.append(mediana)
                ingredientesm.append(jamon)
                ingredientesm.append(pimenton)
                ingredientesm.append(doble_queso)
                ingredientesm.append(aceitunas)
                ingredientesm.append(pepperoni)
                ingredientesm.append(salchichon)
                ingredientesm.append(champiñones)    
                print(ingredientesm)
                ingredientesm = []
                mediana = 0
                champiñones = 0
                jamon = 0
                pimenton = 0
                doble_queso = 0
                aceitunas = 0
                pepperoni = 0
                salchichon = 0
    
    def p_familiar (self):

        familiar = 0
        champiñones = 0
        jamon = 0
        pimenton = 0
        doble_queso = 0
        aceitunas = 0
        pepperoni = 0
        salchichon = 0
        ingredientesf = []
        
        for pizza in self.archivo:
    
            if pizza.count("familiar") == 1:
        
                familiar += pizza.count("familiar")
                jamon += pizza.count("jam")
                pimenton += pizza.count("pimen")
                doble_queso += pizza.count ("doble queso")
                aceitunas += pizza.count("aceitunas")
                pepperoni += pizza.count("pepperoni")
                salchichon += pizza.count("salchi")
                champiñones += pizza.count("champ")
                ingredientesf.append(familiar)
                ingredientesf.append(jamon)
                ingredientesf.append(pimenton)
                ingredientesf.append(doble_queso)
                ingredientesf.append(aceitunas)
                ingredientesf.append(pepperoni)
                ingredientesf.append(salchichon)
                ingredientesf.append(champiñones)
                print(ingredientesf)
                ingredientesf = []
                familiar = 0
                champiñones = 0
                jamon = 0
                pimenton = 0
                doble_queso = 0
                aceitunas = 0
                pepperoni = 0
                salchichon = 0

#prueba de la logica para poder realizar las clases 
f = open ("pedidos1.pz", "r")
c = f.readlines()
b = Cliente(c)
b.datos_cliente()
d = Tipo_pizza(c)
print ("Pedidos Pizza Personal")
d.p_personal()
print ("Pedidos Pizza Mediana")
d.p_mediana()
print ("Pedidos Pizza Familiar")
d.p_familiar()


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