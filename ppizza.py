#Esta Clase recibe de la base de datos las entidades personal, mediana y familiar y 
# calcula por cada una de ellas el numero de pedidos y el monto total
import sqlite3

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