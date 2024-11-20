# Invocar las librerias o modulos

import mysql.connector
from mysql.connector import Error
def conectar_a_basededatos():
    try:
        conexion = mysql.connector.connect(
            host='srv863.hstgr.io',
            password='=3v@/pqWGUJ',
            user='u484426513_ufpic324',
            database='u484426513_ufpic324'
        )
        
        if conexion.is_connected():
            print("Nos hemos conectado al server srv863.hstgr.io")
         
        #obtener la database
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE();")   
        nombredebasedatos = cursor.fetchone()
        print(f"Nombre de la base de datos {nombredebasedatos[0]}")
        #cursor.exec????    
            
            
    #SELECT `id`, `nombre`, `apellido`, `telefono`, `correo` FROM `profesor` WHERE 1            
       
    except Error as e:
        print(f"Error {e}")
        
    finally:    
        #cerrar la connexion
        if conexion.is_connected():
            conexion.close()
            print("se cerro la conexion")
            #conexiones para cerrar
            
            
conectar_a_basededatos()            


