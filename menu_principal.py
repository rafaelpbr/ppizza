import os
import crear_archivo as archivo
import database_pizza as db
from ppizza import *

def menu():
    """limpiar pantalla (válido para windows)"""
    os.system('cls')
    """Opciones del menú"""
    print ("---------- PIZZATON ----------\n")
    print ("------------ Menú ------------\n")
    print ("1 - Cargar Pedidos")
    print ("2 - Generar Resumen de Operaciones")
    print ("3 - Leer archivo resumen")
    print ("4 - Mostrar las tablas de la base de datos")
    print ("5 - Cambiar precios")
    print ("9 - salir")
    print ("\n------------------------------")

def menu2():
    """limpiar pantalla (válido para windows)"""
    #os.system('cls')
    """Opciones del menú"""
    print ("\n")
    print ("1 - Volver")
    #print ("2 - Salir")
    #print ("\n------------------------------")



while True:
    """mostrar menú e ingresar opción"""
    menu()
    opcion = input("elija una opción: ")

    """acciones por cada opción"""
    if opcion == "1": #--------------------------------------------------------- OPCIÓN 1 MENU PRINCIPAL------------------------------------------------------------------------
        print("")
        
        nombre_archivo = input("Eligió: Cargar Pedidos\nColoque el nombre del Archivo que desea procesar junto con su extención: ")
        if nombre_archivo == "":
            print("El archivo introducido no existe: ")
            input("\nSi desea volver al menú principal, marque enter")
        elif nombre_archivo.count(".pz") == 0:
            print("El archivo introducido no existe: ")
            input("\nSi desea volver al menú principal, marque enter")
        else:
            f = open (nombre_archivo, "r")
            c = f.readlines()
            f.close()
            d = Pizza(c)
            d.pedido_cliente()
            input("\nDesea volver al menú principal, marque enter")

        
        
        
    elif opcion == "2": #------------------------------------------------------- OPCIÓN 2 MENU PRINCIPAL------------------------------------------------------------------------
        print("")
        #print("Generando archivo...")
        database = "pizzadb.db"
        conn = db.create_connection(database)
        archivo.select_archivo(conn)
        os.system('cls')
        print("\n¡Archivo generado con éxito!")
        #desde aquí
        while True:
            """submenu de la opcion dos"""
            menu2()
            opcion = input("elija una opción: ")

            """acciones por cada opción"""
            if opcion == "1":
                print("")
                menu()
                break                        
            else:
                input("Opción inválida\npulsa enter para continuar")
                os.system('cls')
        #hasta aquí
        
    elif opcion == "3": #------------------------------------------------------- OPCIÓN 3 MENU PRINCIPAL------------------------------------------------------------------------
        print("")
        input("Leer el Archivo Resumen\npulsa enter para continuar")
        f = open("reporte.pz", "r")
        d = f.read()
        print (d)
        input("\nDesea volver al menú principal, marque enter")
    elif opcion == "4": #------------------------------------------------------- OPCIÓN 4 MENU PRINCIPAL------------------------------------------------------------------------
        print("")
        input("Eligió: Eliminar un pedido\npulsa enter para continuar")
    elif opcion == "5": #------------------------------------------------------- OPCIÓN 5 MENU PRINCIPAL------------------------------------------------------------------------
        print("")
        input("Eligió: Cambiar precios\npulsa enter para continuar")
    elif opcion == "9": #------------------------------------------------------- OPCIÓN 9 MENU PRINCIPAL------------------------------------------------------------------------
        break
    else:
        input("Opción inválida\npulsa enter para continuar")

