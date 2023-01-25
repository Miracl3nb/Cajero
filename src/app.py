#logeo
import mysql.connector




def logeo ():
    clientedni = input("Ingrese su Dni: ")



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
        clientedni = input("Ingrese su Dni: ")
        cursor = connection.cursor()
        sql = "SELECT * FROM cuentas WHERE DNI='{}'".format(clientedni)
        cursor.execute(sql)
        registronombre = cursor.fetchall()
        for x in registronombre:        
            print(f"Bienvenido, {x[3]}")
            consultapin = int(input("Igrese su PIN: "))
            if consultapin == (x[2]):
                print("Acceso Correcto")
            else:
                print("PIN incorrecta")
            
            
except Exception as ex:
    print(ex)
    

"""    
        clientepin = input("Ingrese su pin: ")
        consultapin = "SELECT PIN FROM cuentas WHERE DNI = '{}'".format(clientedni)
        pinsql = cursor.execute(consultapin)
        registropin = cursor.fetchone()
        print(registropin)
        
        
        
    if registro:
            sqlnombre = cursor.execute("SELECT NOMBRE FROM cuentas WHERE DNI = '{}'".format(clientedni))
            print(f"Bienvenido {sqlnombre}")       

        #consultadni = cursor.execute("SELECT IF (EXISTS(SELECT NOMBRE FROM cuentas WHERE DNI = 36398721), 1, 0);")
        print(cursor.execute("SELECT IF (EXISTS(SELECT NOMBRE FROM cuentas WHERE DNI = 36398721), 'existe', 'no existe');"))
        
        if consultadni == "1":
            nombreprint = cursor.execute(f"SELECT NOMBRE FROM cuentas WHERE DNI ={clientedni};")
            print(f"Bienvenido/a {nombreprint}")
            clientepin = int(input("Coloque su PIN: "))
            pin = cursor.execute(f"SELECT PIN FROM cuentas WHERE DNI = {clientedni};")
            if clientepin == pin:
                print("Conexion Correcta!")
            else:
                print("Conexion Incorrecta")
        else:
            print("Dni no encontrado")  
"""
