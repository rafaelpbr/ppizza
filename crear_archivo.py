import sqlite3
from sqlite3 import Error
import database_pizza as db
import os 


""" select para el archivo """
def select_archivo(conn):
        
    cur = conn.cursor()
    cur.execute("select e.fecha, i.tamano, i.jamon, i.champinon, i.pimenton, i.dob_queso, i.aceitunas, i.pepperoni, i.salchichon from pedido e, pizza i where e.id = i.id_pedido order by e.fecha")
    cur_one = conn.cursor()
    cur_one.execute("select e.fecha from pedido e, pizza i where e.id = i.id_pedido order by e.fecha")


    row_one = cur_one.fetchone() 
    rows = cur.fetchall()


    for row in row_one:
        fechaanterior = row
        
    
    
    global p_pizza 
    global p_jamon 
    global p_champinon 
    global p_pimenton 
    global p_dob_queso
    global p_aceitunas
    global p_pepperoni
    global p_salchichon 
    global m_pizza 
    global m_jamon
    global m_champinon 
    global m_pimenton 
    global m_dob_queso
    global m_aceitunas
    global m_pepperoni
    global m_salchichon 
    global f_pizza 
    global f_jamon 
    global f_champinon 
    global f_pimenton 
    global f_aceitunas 
    global f_pepperoni 
    global f_salchichon
    global f_dob_queso

    p_pizza = 0
    p_jamon = 0
    p_champinon = 0
    p_pimenton = 0
    p_dob_queso = 0
    p_aceitunas = 0
    p_pepperoni = 0
    p_salchichon = 0
    m_pizza = 0
    m_jamon = 0
    m_champinon = 0
    m_pimenton = 0
    m_dob_queso = 0
    m_aceitunas = 0
    m_pepperoni = 0
    m_salchichon = 0
    f_pizza = 0
    f_jamon = 0
    f_champinon = 0
    f_pimenton = 0
    f_aceitunas = 0
    f_pepperoni = 0
    f_salchichon = 0
    f_dob_queso = 0

    file = open("./reporte.pz","w")
 
    for row in rows:

        fecha = row[0]
        tamano = row[1]

        if fechaanterior == fecha:
            if tamano == 'personal':
                p_pizza += 1
                p_jamon = p_jamon + row[2]
                p_champinon = p_champinon + row[3]
                p_pimenton = p_pimenton + row[4]
                p_dob_queso = p_dob_queso + row[5]
                p_aceitunas = p_aceitunas + row[6]
                p_pepperoni = p_pepperoni + row[7]
                p_salchichon = p_salchichon + row[8]
            elif tamano == 'mediana':
                m_pizza += 1
                m_jamon = m_jamon + row[2]
                m_champinon = m_champinon + row[3]
                m_pimenton = m_pimenton + row[4]
                m_dob_queso = m_dob_queso + row[5]
                m_aceitunas = m_aceitunas + row[6]
                m_pepperoni = m_pepperoni + row[7]
                m_salchichon = m_salchichon + row[8]
            elif tamano == 'familiar':
                f_pizza += 1
                f_jamon = f_jamon + row[2]
                f_champinon = f_champinon + row[3]
                f_pimenton = f_pimenton + row[4]
                f_dob_queso = f_dob_queso + row[5]
                f_aceitunas = f_aceitunas + row[6]
                f_pepperoni = f_pepperoni + row[7]
                f_salchichon = f_salchichon + row[8]
            
            #print(rows.index(row),'de',len(rows)-1) 
            if rows.index(row) == len(rows)-1:
                unid_jamon = p_jamon + m_jamon + f_jamon
                unid_champinon = p_champinon + m_champinon + f_champinon
                unid_pimenton = p_pimenton + m_pimenton + f_pimenton 
                unid_dob_queso = p_dob_queso + m_dob_queso + f_dob_queso 
                unid_aceitunas = p_aceitunas + m_aceitunas + f_aceitunas 
                unid_pepperoni = p_pepperoni + m_pepperoni + f_pepperoni 
                unid_salchichon = p_salchichon + m_salchichon + f_salchichon 

                monto_pizzap = p_pizza*db.price_pizza.get('personal')
                monto_pizzam = m_pizza*db.price_pizza.get('mediana')
                monto_pizzaf = f_pizza*db.price_pizza.get('familiar')
                monto_jamon = p_jamon*db.price_jamon.get('personal') + m_jamon*db.price_jamon.get('mediana') + f_jamon*db.price_jamon.get('familiar')
                monto_champinon = p_champinon*db.price_champinon.get('personal') + m_champinon*db.price_champinon.get('mediana') + f_champinon*db.price_champinon.get('familiar')
                monto_pimenton = p_pimenton*db.price_pimenton.get('personal') + m_pimenton*db.price_pimenton.get('mediana') + f_pimenton*db.price_pimenton.get('familiar')
                monto_dob_queso = p_dob_queso*db.price_dob_queso.get('personal') + m_dob_queso*db.price_dob_queso.get('mediana') + f_dob_queso*db.price_dob_queso.get('familiar') 
                monto_aceitunas = p_aceitunas*db.price_aceitunas.get('personal') + m_aceitunas*db.price_aceitunas.get('mediana') + f_aceitunas*db.price_aceitunas.get('familiar') 
                monto_pepperoni = p_pepperoni*db.price_pepperoni.get('personal') + m_pepperoni*db.price_pepperoni.get('mediana') + f_pepperoni*db.price_pepperoni.get('familiar') 
                monto_salchichon = p_salchichon*db.price_salchichon.get('personal') + m_salchichon*db.price_salchichon.get('mediana') + f_salchichon*db.price_salchichon.get('familiar') 
                monto_total = monto_pizzap + monto_pizzam + monto_pizzaf + monto_jamon + monto_champinon + monto_pimenton + monto_dob_queso + monto_aceitunas + monto_pepperoni + monto_salchichon

                file.write('\nFecha: '+fechaanterior+os.linesep)
                #print('\t')
                file.write('Venta Total: '+"{0:.2f}".format(monto_total)+' UMs'+ os.linesep)
                #print('\t')

                file.write('Ventas por pizza (sin incluir adicionales): '+ os.linesep)
                file.write(f"{'Tamano'.ljust(14)}"+f"{'Unidades'.ljust(15)}"+'Monto UMs'+ os.linesep)
                file.write(f"{'Personal'.ljust(15)}"+f"{str(p_pizza).ljust(15)}"+ "{0:.2f}".format(monto_pizzap) + os.linesep)
                file.write(f"{'Mediana'.ljust(15)}"+f"{str(m_pizza).ljust(15)}"+ "{0:.2f}".format(monto_pizzam) + os.linesep)
                file.write(f"{'Familiar'.ljust(15)}"+f"{str(f_pizza).ljust(15)}"+ "{0:.2f}".format(monto_pizzaf) + os.linesep)
                #print('\t')

                file.write('Ventas por Ingrediente: '+ os.linesep)
                file.write(f"{'Ingredientes'.ljust(15)}"+f"{'Unidades'.ljust(15)}"+'Monto UMs' + os.linesep)
                file.write(f"{'Jamon'.ljust(15)}"+f"{str(unid_jamon).ljust(15)}" + "{0:.2f}".format(monto_jamon) + os.linesep)
                file.write(f"{'Champinones'.ljust(15)}" + f"{str(unid_champinon).ljust(15)}" + "{0:.2f}".format(monto_champinon) + os.linesep)
                file.write(f"{'Pimenton'.ljust(15)}"+f"{str(unid_pimenton).ljust(15)}" + "{0:.2f}".format(monto_pimenton) + os.linesep)
                file.write(f"{'Doble Queso'.ljust(15)}"+f"{str(unid_dob_queso).ljust(15)}" + "{0:.2f}".format(monto_dob_queso) + os.linesep)
                file.write(f"{'Aceitunas'.ljust(15)}"+f"{str(unid_aceitunas).ljust(15)}" + "{0:.2f}".format(monto_aceitunas) + os.linesep)
                file.write(f"{'Pepperoni'.ljust(15)}"+f"{str(unid_pepperoni).ljust(15)}" + "{0:.2f}".format(monto_pepperoni) + os.linesep)
                file.write(f"{'Salchichon'.ljust(15)}"+f"{str(unid_salchichon).ljust(15)}" + "{0:.2f}".format(monto_salchichon) + os.linesep)
                file.write('---------------------------------------------' + os.linesep)
                #print('\n')


        else:
            unid_jamon = p_jamon + m_jamon + f_jamon
            unid_champinon = p_champinon + m_champinon + f_champinon
            unid_pimenton = p_pimenton + m_pimenton + f_pimenton 
            unid_dob_queso = p_dob_queso + m_dob_queso + f_dob_queso 
            unid_aceitunas = p_aceitunas + m_aceitunas + f_aceitunas 
            unid_pepperoni = p_pepperoni + m_pepperoni + f_pepperoni 
            unid_salchichon = p_salchichon + m_salchichon + f_salchichon 

            monto_pizzap = p_pizza*db.price_pizza.get('personal')
            monto_pizzam = m_pizza*db.price_pizza.get('mediana')
            monto_pizzaf = f_pizza*db.price_pizza.get('familiar')
            monto_jamon = p_jamon*db.price_jamon.get('personal') + m_jamon*db.price_jamon.get('mediana') + f_jamon*db.price_jamon.get('familiar')
            monto_champinon = p_champinon*db.price_champinon.get('personal') + m_champinon*db.price_champinon.get('mediana') + f_champinon*db.price_champinon.get('familiar')
            monto_pimenton = p_pimenton*db.price_pimenton.get('personal') + m_pimenton*db.price_pimenton.get('mediana') + f_pimenton*db.price_pimenton.get('familiar')
            monto_dob_queso = p_dob_queso*db.price_dob_queso.get('personal') + m_dob_queso*db.price_dob_queso.get('mediana') + f_dob_queso*db.price_dob_queso.get('familiar') 
            monto_aceitunas = p_aceitunas*db.price_aceitunas.get('personal') + m_aceitunas*db.price_aceitunas.get('mediana') + f_aceitunas*db.price_aceitunas.get('familiar') 
            monto_pepperoni = p_pepperoni*db.price_pepperoni.get('personal') + m_pepperoni*db.price_pepperoni.get('mediana') + f_pepperoni*db.price_pepperoni.get('familiar') 
            monto_salchichon = p_salchichon*db.price_salchichon.get('personal') + m_salchichon*db.price_salchichon.get('mediana') + f_salchichon*db.price_salchichon.get('familiar') 
            monto_total = monto_pizzap + monto_pizzam + monto_pizzaf + monto_jamon + monto_champinon + monto_pimenton + monto_dob_queso + monto_aceitunas + monto_pepperoni + monto_salchichon

            file.write('\nFecha: ' + fechaanterior + os.linesep)
            #print('\t')
            file.write('Venta Total: '+ "{0:.2f}".format(monto_total)+ ' UMs' + os.linesep)
            #print('\t')

            file.write('Ventas por pizza (sin incluir adicionales): '+ os.linesep)
            file.write(f"{'Tamano'.ljust(14)}"+f"{'Unidades'.ljust(15)}"+'Monto UMs'+ os.linesep)
            file.write(f"{'Personal'.ljust(15)}"+f"{str(p_pizza).ljust(15)}"+ "{0:.2f}".format(monto_pizzap) + os.linesep)
            file.write(f"{'Mediana'.ljust(15)}"+f"{str(m_pizza).ljust(15)}"+ "{0:.2f}".format(monto_pizzam) + os.linesep)
            file.write(f"{'Familiar'.ljust(15)}"+f"{str(f_pizza).ljust(15)}"+ "{0:.2f}".format(monto_pizzaf) + os.linesep)
            #print('\t')

            file.write('Ventas por Ingrediente: '+ os.linesep)
            file.write(f"{'Ingredientes'.ljust(15)}"+f"{'Unidades'.ljust(15)}"+'Monto UMs' + os.linesep)
            file.write(f"{'Jamon'.ljust(15)}"+f"{str(unid_jamon).ljust(15)}" + "{0:.2f}".format(monto_jamon) + os.linesep)
            file.write(f"{'Champinones'.ljust(15)}" + f"{str(unid_champinon).ljust(15)}" + "{0:.2f}".format(monto_champinon) + os.linesep)
            file.write(f"{'Pimenton'.ljust(15)}"+f"{str(unid_pimenton).ljust(15)}" + "{0:.2f}".format(monto_pimenton) + os.linesep)
            file.write(f"{'Doble Queso'.ljust(15)}"+f"{str(unid_dob_queso).ljust(15)}" + "{0:.2f}".format(monto_dob_queso) + os.linesep)
            file.write(f"{'Aceitunas'.ljust(15)}"+f"{str(unid_aceitunas).ljust(15)}" + "{0:.2f}".format(monto_aceitunas) + os.linesep)
            file.write(f"{'Pepperoni'.ljust(15)}"+f"{str(unid_pepperoni).ljust(15)}" + "{0:.2f}".format(monto_pepperoni) + os.linesep)
            file.write(f"{'Salchichon'.ljust(15)}"+f"{str(unid_salchichon).ljust(15)}" + "{0:.2f}".format(monto_salchichon) + os.linesep)
            file.write('---------------------------------------------' + os.linesep)
            #print('\n')
                

            if tamano == 'personal':
                p_pizza = 1
                p_jamon = row[2]
                p_champinon = row[3]
                p_pimenton = row[4]
                p_dob_queso = row[5]
                p_aceitunas = row[6]
                p_pepperoni = row[7]
                p_salchichon = row[8]
            elif tamano == 'mediana':
                m_pizza = 1
                m_jamon = row[2]
                m_champinon = row[3]
                m_pimenton = row[4]
                m_dob_queso = row[5]
                m_aceitunas = row[6]
                m_pepperoni = row[7]
                m_salchichon = row[8]
            elif tamano == 'familiar':
                f_pizza = 1
                f_jamon = row[2]
                f_champinon = row[3]
                f_pimenton = row[4]
                f_dob_queso = row[5]
                f_aceitunas = row[6]
                f_pepperoni = row[7]
                f_salchichon = row[8]            

        
        fechaanterior = fecha

    file.close()


# -------------------------------------------------------------------------------------------------------------------------------------------


def main():
    database = "pizzadb.db"
 
    """Conexión a la base de datos"""
    conn = db.create_connection(database)
    with conn:
                
        select_archivo(conn)

if __name__ == "__main__":
    main()