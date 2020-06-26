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
        lfin = []
        cont = self.tamaño()
        comi = self.comienzo()
        for i in comi:
            if i == 0:
                continue
            lfin.append(i-1)    
        return lfin  
#Recorre el archivo tomando en cuenta     
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
        comienzo = self.comienzo()
        fin = self.final()
        pedidos = len(comienzo) - 1
        for i in range(int(pedidos)):
            print ("\nPedido: ", i)
            for j in range (int(comienzo[i])+1,int(fin[i])):
                linea = self.archivo[j]
                if linea.count("personal"):
                    jamon += linea.count("jam")
                    pimenton += linea.count("pimen")
                    doble_queso += linea.count ("doble queso")
                    aceitunas += linea.count("aceitunas")
                    pepperoni += linea.count("pepperoni")
                    salchichon += linea.count("salchi")
                    champiñones += linea.count("champ")
                    print("esta persona pidio una pizza personal con: ", jamon, " jamon ", pimenton, " pimenton ", doble_queso, 
                        " doble queso ", aceitunas, " aceitunas ", pepperoni, " pepproni ", salchichon, " salchichon ", champiñones, " champiñones" )
                    personal = 0
                    champiñones = 0
                    jamon = 0
                    pimenton = 0
                    doble_queso = 0
                    aceitunas = 0
                    pepperoni = 0
                    salchichon = 0
                if linea.count("mediana"):
                    jamon += linea.count("jam")
                    pimenton += linea.count("pimen")
                    doble_queso += linea.count ("doble queso")
                    aceitunas += linea.count("aceitunas")
                    pepperoni += linea.count("pepperoni")
                    salchichon += linea.count("salchi")
                    champiñones += linea.count("champ")
                    print("esta persona pidio una pizza mediana con: ", jamon, " jamon ", pimenton, " pimenton ", doble_queso, 
                        " doble queso ", aceitunas, " aceitunas ", pepperoni, " pepproni ", salchichon, " salchichon ", champiñones, " champiñones" )
                    personal = 0
                    champiñones = 0
                    jamon = 0
                    pimenton = 0
                    doble_queso = 0
                    aceitunas = 0
                    pepperoni = 0
                    salchichon = 0
                if linea.count("familiar"):
                    jamon += linea.count("jam")
                    pimenton += linea.count("pimen")
                    doble_queso += linea.count ("doble queso")
                    aceitunas += linea.count("aceitunas")
                    pepperoni += linea.count("pepperoni")
                    salchichon += linea.count("salchi")
                    champiñones += linea.count("champ")
                    print("esta persona pidio una pizza familiar con: ", jamon, " jamon ", pimenton, " pimenton ", doble_queso, 
                        " doble queso ", aceitunas, " aceitunas ", pepperoni, " pepproni ", salchichon, " salchichon ", champiñones, " champiñones" )
                    personal = 0
                    champiñones = 0
                    jamon = 0
                    pimenton = 0
                    doble_queso = 0
                    aceitunas = 0
                    pepperoni = 0
                    salchichon = 0
            

        



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

f = open ("pedidos1.pz", "r")
c = f.readlines()
d = Pedido(c)
b = Cliente(c)
d.pedido_cliente()