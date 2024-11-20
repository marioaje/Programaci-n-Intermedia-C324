# Invocar las librerias o modulos

import mysql.connector
from mysql.connector import Error
def testconectar_a_basededatos():
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
         #SELECT `id`, `nombre`, `apellido`, `telefono`, `correo` FROM `profesor` WHERE 1 
        nombredebasedatos = cursor.fetchone()
        print(f"Nombre de la base de datos {nombredebasedatos[0]}")
        #cursor.exec????    
          
    except Error as e:
        print(f"Error {e}")
        
    finally:    
        #cerrar la connexion
        if conexion.is_connected():
            conexion.close()
            print("se cerro la conexion")
            #conexiones para cerrar



def conectar_a_basededatos():
    try:
        conexion = mysql.connector.connect(
            host='srv863.hstgr.io',
            password='=3v@/pqWGUJ',
            user='u484426513_ufpic324',
            database='u484426513_ufpic324'
        )
        if conexion.is_connected():
            return conexion
          
    except Error as e:
        print(f"Error {e}")        

            
def consultar_profesor():
    conexion = conectar_a_basededatos()    
    
    if conexion:
        
        try:
            cursor = conexion.cursor(dictionary=True)
            consulta = 'SELECT `id`, `nombre`, `apellido`, `telefono`, `correo` FROM `profesor`'
            cursor.execute(consulta) 

            resultado = cursor.fetchall()
            
            print("Datos de los profes o tabla profesor")
            print('`id` | `nombre` | `apellido` | `telefono` | `correo`')
            print('**'*20)
            
            for fila in resultado:
                print(f"ID: { fila['id'] } | nombre: {fila['nombre']} | apellido: {fila['apellido' ]} | telofono: {fila['telefono']} | correo: {fila['correo']}")
                #print(f"ID: { fila['id'] } | {fila['nombre']} | {fila['apellido']} | {fila['telefono']} | {fila['correo']}")
            
            
        except Error as e:
            print(f"Error {e}")
            
        finally:    
            #cerrar la connexion
            if conexion.is_connected():
                conexion.close()
                print("se cerro la conexion")
                #conexiones para cerrar           
            
            
            
            
#testconectar_a_basededatos()          
consultar_profesor()


