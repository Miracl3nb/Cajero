from typing import Self
import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host ='localhost',
                port =3306,
                user= 'root',
                password = 'P@ss1961!!',
                db = 'cuentasclientes'
                
        )
        except Error as ex:
            print("Error al intenar conectar {0}".format(ex))
    
    def login (self):
        if self.conexion.is_connected():
            try:
                cur = self.connetion.cursor()
                clientedni = int(input("Ingrese su dni: "))
                sqlcon = "SELECT * FROM cuentas WHERE DNI='{}'".format(clientedni)
                cur.execute(sqlcon)
                sqlregi = cur.fechall()
                for i in sqlregi:
                    dni = i[1]
                    pin = i[2]
                    nombre = i[3]
                    
                if dni == clientedni:
                    print(f"Bienvenido/a {nombre}")
                    clientepin = int(input("Ingrese su PIN: "))
                    if pin == clientedni:
                        print("Ingreso Correcto")
                        #mandar funcion de menu usuario
        
            except Error as ex:
                print("Error al intenar conectar {0}".format(ex))
            
        
        