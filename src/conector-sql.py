import mysql.connector

def conexion():
    try:
        connection=mysql.connector.connect(
            host ='localhost',
            port =3306,
            user= 'root',
            password = 'P@ss1961!!',
            db = 'cuentasclientes'
        )
        
        if connection.is_connected():
            print("Conexion correcta")
            infoServer = connection.get_server_info()
            print(infoServer)
        clientedni = input("Ingrese su Dni: ")
        cursor = connection.cursor()
        sql = "SELECT * FROM cuentas WHERE DNI='{}'".format(clientedni)
        cursor.execute(sql)
        registronombre = cursor.fetchall()
        for x in registronombre:
            for x in registronombre:        
                print(f"Bienvenido, {x[3]}")
            consultapin = int(input("Igrese su PIN: "))
            if consultapin == (x[2]):
                print("Acceso Correcto")
            else:
                print("PIN incorrecta")  
                print(f"dni = {x[1]}, pin ={x[2]}, nombre = {x[3]}, saldo = {x[4]}")  
            #if dni == clientedni:
            #    print(f"Bienvenido, {nombre}")
            #    consultapin = int(input("Igrese su PIN: "))
            #    if consultapin == pin:
            #       print("Acceso Correcto")
            #    else:
            #        print("PIN incorrecta")


    except Exception as ex:
        print(ex)


#def logeo ():
    clientedni = input("Ingrese su Dni: ")
    #cursor = connection.cursor()
    sql = "SELECT * FROM cuentas WHERE DNI='{}'".format(clientedni)
    cursor.execute(sql)
    registronombre = cursor.fetchall()
    for x in registronombre:        
        if clientedni == x[1]:
            print(f"Bienvenido, {x[3]}")
            consultapin = int(input("Igrese su PIN: "))
            if consultapin == (x[2]):
                    print("Acceso Correcto")
            else:
                    print("PIN incorrecta")
        else:
            print("Usuario no registrado")


conexion()

