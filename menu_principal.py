import os

def menu():
    """limpiar pantalla (válido para windows)"""
    os.system('cls')
    """Opciones del menú"""
    print ("------------ Menú ------------\n")
    print ("1 - Cargar Pedidos")
    print ("2 - Generar Reporte del día")
    print ("3 - Ver Ranking de clientes")
    print ("4 - Eliminar un pedido")
    print ("5 - Cambiar precios")
    print ("9 - salir")
    print ("\n------------------------------")

while True:
    """mostrar menú e ingresar opción"""
    menu()
    opcion = input("elija una opción: ")

    """acciones por cada opción"""
    if opcion == "1":
        print("")
        input("Eligió: Cargar Pedidos\npulsa enter para continuar")
    elif opcion == "2":
        print("")
        input("Eligió: Generar Reporte del día\npulsa enter para continuar")
    elif opcion == "3":
        print("")
        input("Eligió: Ver Ranking de clientes\npulsa enter para continuar")
    elif opcion == "4":
        print("")
        input("Eligió: Eliminar un pedido\npulsa enter para continuar")
    elif opcion == "5":
        print("")
        input("Eligió: Cambiar precios\npulsa enter para continuar")
    elif opcion == "9":
        break
    else:
        input("Opción inválida\npulsa enter para continuar")

