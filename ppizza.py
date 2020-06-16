#Esta Clase recibe de la base de datos las entidades personal, mediana y familiar y 
# calcula por cada una de ellas el numero de pedidos y el monto total
import sqlite3

class Clientes ():
    
    def __init__(self, personal= None, mediana=None, familiar=None ):
        self.personal = personal
        self.mediana = mediana
        self.familiar = familiar
    
    def cont_personal (self):
              
              count = 0
              unidades = self.personal.fetchall()
              for unidad in unidades:
                  count += 1

              monto = count*10
              return count, monto
    
    def cont_mediana (self):
              
              count = 0
              unidades = self.mediana.fetchall()
              for unidad in unidades:
                  count += 1

              monto = count*15
              return count, monto
    
    def cont_familiar (self):
              
              count = 0
              unidades = self.familiar.fetchall()
              for unidad in unidades:
                  count += 1

              monto = count*20
              return count, monto

#Esta Clase recibe de la base de datos la entidad ingredientes la cual tiene la columna par para el ingrediente y el tipo de pizza 
# calcula por ingrediente el monto 

class Ingredientes ():

    def __init__(self,ingredientes):
        