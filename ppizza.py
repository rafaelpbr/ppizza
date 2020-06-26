import database_pizza as db

#Esta clase tiene de atributos el tamaño del archivo y el comienzo y el final de cada pedido
class Pedido():

    def __init__(self, archivo):
        self.archivo = archivo

#Calcula el tamaño del pedido, esto sirve para recorrer la lista que se crea para leer el archivo
    def tamaño(self):
        tam = len(self.archivo)
        return tam
#Calculo el comienzo del indice del comienzo del pedido
    def comienzo(self):
    
        lcomienzo = []
        lfin = []
        cont = self.tamaño()
        for i in range(int(cont)):
            if self.archivo[0] == self.archivo[i]:
                lcomienzo.append(i)
        return lcomienzo
    
#Calcula el indice del fin del pedido, con esto y el metodo anterior se puede recorrer el archivo iterando solo entre los pedidos, para recoger los datos por persona     
    def final(self):
    
        lcomienzo = self.comienzo()
        ultimo = self.tamaño()
        lfin = []
        cont = self.tamaño()
        comi = self.comienzo()
        for i in comi:
            if i == 0:
                if cont <= 4:
                    lfin.append(int(cont))
                    continue
                else:
                    continue
            lfin.append(i-1)
        if cont >> 4:
            lfin.append(ultimo)

        return lfin  
#Recorre el archivo tomando en cuenta     

class Cliente (Pedido):

    def __init__ (self, archivo):
        Pedido.__init__(self, archivo)
    
    def nombre (self):

        comie = Pedido.comienzo(self) 
        linea = ""
        nombre = ""
        list_nombre = []
        for i in comie:
            linea = self.archivo[i+1]
            indice = linea.find(";")
            if indice == 0:
                nombre = "Este cliente no tiene nombre"
                list_nombre.append(nombre)
                continue
            nombre = linea[:int(indice)]
            list_nombre.append(nombre)
        return list_nombre

    def fecha (self):

        comie = Pedido.comienzo(self) 
        linea = ""
        fecha = ""
        list_fecha = []
        for i in comie:
            linea = self.archivo[i+1]
            indice = linea.find(";")
            ultimo = len(linea)
            fecha = linea [int(indice)+1:int(ultimo)-1]
            list_fecha.append(fecha)
        return list_fecha

class Pizza (Cliente):
    
    def __init__(self, archivo):
        Pedido.__init__(self, archivo)

    def pedido_cliente (self):

        linea = ""
        personal = 0
        champiñones = 0
        jamon = 0
        pimenton = 0
        doble_queso = 0
        aceitunas = 0
        pepperoni = 0
        salchichon = 0
        monto = 0
        total = 0
        namec = Cliente.nombre(self)
        datec = Cliente.fecha(self)
        comienzo = Pedido.comienzo(self)
        fin = Pedido.final(self)
        if comienzo[0] == 0:
            pedidos = len(comienzo) 
        else:
            pedidos = len(comienzo) - 1
        for i in range(int(pedidos)):
            print ("--------------------------------\nCliente: ", namec[i])
            print("Fecha: ", datec[i])
            db.insertar_nuevo_pedido(datec[i],namec[i])
            for j in range (int(comienzo[i])+1,int(fin[i])):
                linea = self.archivo[j]
                if linea.count("personal"):
                    print("Tipo de pizza: Personal")
                    print("Ingredientes Adicional:")
                    jamon += linea.count("jam")
                    if jamon != 0:
                        print ("Jamon")
                    pimenton += linea.count("pimen")
                    if pimenton != 0:
                        print ("Pimenton")
                    doble_queso += linea.count ("doble queso")
                    if doble_queso != 0:
                        print ("Doble Queso")
                    aceitunas += linea.count("aceitunas")
                    if aceitunas != 0:
                        print ("Aceitunas")
                    pepperoni += linea.count("pepperoni")
                    if pepperoni != 0:
                        print ("Pepperoni")
                    salchichon += linea.count("salchi")
                    if salchichon != 0:
                        print ("Salchichon")
                    champiñones += linea.count("champ")
                    if champiñones != 0:
                        print ("champiñones")
                    db.insertar_nueva_pizza('personal', jamon, champiñones, pimenton, doble_queso, aceitunas, pepperoni, salchichon)
                    monto = 10 + jamon*1.5 + pimenton*1.5 + doble_queso*0.80 + aceitunas*1.80 + pepperoni*1.25 + salchichon*1.60 + champiñones*1.75
                    total = total + monto
                    personal = 0
                    champiñones = 0
                    jamon = 0
                    pimenton = 0
                    doble_queso = 0
                    aceitunas = 0
                    pepperoni = 0
                    salchichon = 0
                    monto = 0
                if linea.count("mediana"):
                    print("Tipo de pizza: Personal")
                    print("Ingredientes Adicional:")
                    jamon += linea.count("jam")
                    if jamon != 0:
                        print ("Jamon")
                    pimenton += linea.count("pimen")
                    if pimenton != 0:
                        print ("Pimenton")
                    doble_queso += linea.count ("doble queso")
                    if doble_queso != 0:
                        print ("Doble Queso")
                    aceitunas += linea.count("aceitunas")
                    if aceitunas != 0:
                        print ("Aceitunas")
                    pepperoni += linea.count("pepperoni")
                    if pepperoni != 0:
                        print ("Pepperoni")
                    salchichon += linea.count("salchi")
                    if salchichon != 0:
                        print ("Salchichon")
                    champiñones += linea.count("champ")
                    if champiñones != 0:
                        print ("champiñones")
                    db.insertar_nueva_pizza('mediana', jamon, champiñones, pimenton, doble_queso, aceitunas, pepperoni, salchichon)
                    monto = 15 + jamon*1.75 + pimenton*1.75 + doble_queso*1.30 + aceitunas*2.15 + pepperoni*1.70 + salchichon*1.85 + champiñones*2.05
                    total = total + monto
                    personal = 0
                    champiñones = 0
                    jamon = 0
                    pimenton = 0
                    doble_queso = 0
                    aceitunas = 0
                    pepperoni = 0
                    salchichon = 0
                    monto
                if linea.count("familiar"):
                    print("Tipo de pizza: Familiar")
                    print("Ingredientes Adicional:")
                    jamon += linea.count("jam")
                    if jamon != 0:
                        print ("Jamon")
                    pimenton += linea.count("pimen")
                    if pimenton != 0:
                        print ("Pimenton")
                    doble_queso += linea.count ("doble queso")
                    if doble_queso != 0:
                        print ("Doble Queso")
                    aceitunas += linea.count("aceitunas")
                    if aceitunas != 0:
                        print ("Aceitunas")
                    pepperoni += linea.count("pepperoni")
                    if pepperoni != 0:
                        print ("Pepperoni")
                    salchichon += linea.count("salchi")
                    if salchichon != 0:
                        print ("Salchichon")
                    champiñones += linea.count("champ")
                    if champiñones != 0:
                        print ("champiñones")
                    db.insertar_nueva_pizza('familiar', jamon, champiñones, pimenton, doble_queso, aceitunas, pepperoni, salchichon)
                    monto = 20 + jamon*2 + pimenton*2 + doble_queso*1.70 + aceitunas*2.60 + pepperoni*1.90 + salchichon*2.10 + champiñones*2.50
                    total = total + monto
                    personal = 0
                    champiñones = 0
                    jamon = 0
                    pimenton = 0
                    doble_queso = 0
                    aceitunas = 0
                    pepperoni = 0
                    salchichon = 0
                    monto = 0
            print("Total del Pedido: ", total)
            total = 0

f = open ("E:/Electiva_Python/Proyecto/pedidos1.pz", "r")
c = f.readlines()
d = Pizza(c)
b = Cliente(c)
d.pedido_cliente()