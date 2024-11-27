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
            
            
def insertar_profesor(nombre, apellido, telefono, correo):
    "Insertar datos"
    
    conexion = conectar_a_basededatos()    
    
    if conexion:
        
        try:
            cursor = conexion.cursor()
            consulta = 'INSERT INTO `profesor`(`nombre`, `apellido`, `telefono`, `correo`) VALUES ( %s, %s, %s, %s)'
            
            
            valores = (nombre, apellido, telefono, correo)
            
            cursor.execute(consulta, valores) 

            conexion.commit()#confirmar los cambios o que se guarden los cambios
            
            print(f"Datos del profesor {nombre}, {apellido}, {telefono}, {correo}")
         
            
        except Error as e:
            print(f"Error al insertar datos{e}")
            
        finally:    
            #cerrar la connexion
            if conexion.is_connected():
                conexion.close()
                print("se cerro la conexion")
                #conexiones para cerrar     
                
                
          
def  modificar_profesor(id, nombre, apellido, telefono, correo):
    "Modificar datos"
    
    conexion = conectar_a_basededatos()    
    
    if conexion:
        
        try:
            cursor = conexion.cursor()
            consulta = 'UPDATE `profesor` SET `nombre`= %s,`apellido`= %s,`telefono`= %s,`correo`= %s WHERE id = %s'
           
            valores = (nombre, apellido, telefono, correo, id)
            
            cursor.execute(consulta, valores) 

            conexion.commit()#confirmar los cambios o que se guarden los cambios
            
            print(f"Datos del profesor {id}, {nombre}, {apellido}, {telefono}, {correo}")
         
            
        except Error as e:
            print(f"Error al modificar datos{e}")
            
        finally:    
            #cerrar la connexion
            if conexion.is_connected():
                conexion.close()
                print("se cerro la conexion")
                #conexiones para cerrar                    
                
          
def  eliminar_profesor(id):
    "Eliminar datos"
    
    conexion = conectar_a_basededatos()    
    
    if conexion:
        
        try:
            cursor = conexion.cursor()
            consulta = 'DELETE FROM `profesor` WHERE id = %s'
           
            valores = (id,)
            
            cursor.execute(consulta, valores) 
            conexion.commit()#confirmar los cambios o que se guarden los cambios
            
            if cursor.rowcount > 0:
                print("se elimino")
            else:
                print("No se encontro")

            print(f"Eliminando datos del profesor {id}")
         
            
        except Error as e:
            print(f"Error al eliminar datos{e}")
            
        finally:    
            #cerrar la connexion
            if conexion.is_connected():
                
                conexion.close()
                print("se cerro la conexion")
                #conexiones para cerrar      
                
          
def  consultarid_profesor(id):
    "Consultar datos por ID"
    
    conexion = conectar_a_basededatos()    
    
    if conexion:
        
        try:
            cursor = conexion.cursor()
            consulta = 'SELECT `id`, `nombre`, `apellido`, `telefono`, `correo`  FROM `profesor` WHERE id = %s'
           
            valores = (id,)
            
            cursor.execute(consulta, valores) 
            resultado = cursor.fetchone()
            
            if resultado:
                print(f"Datos del profesor {resultado['id']}")
                # Un diccionario???
                # print(f"Datos del profesor {resultado['id']}, {resultado['nombre']}, {resultado['apellido']}, {resultado['telefono']}, {resultado['correo']}")
                return resultado
            else:
                print("No se encontro el dato")
                return None
            
        except Error as e:
            print(f"Error al eliminar datos{e}")
            
        finally:    
            #cerrar la connexion
            if conexion.is_connected():      
                
                conexion.close()
                print("se cerro la conexion")
                #conexiones para cerrar      
                                                             
 # INSERT INTO `profesor`(`id`, `nombre`, `apellido`, `telefono`, `correo`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]')
 

# DELETE FROM `profesor` WHERE 0


# UPDATE `profesor` SET `id`='[value-1]',`nombre`='[value-2]',`apellido`='[value-3]',`telefono`='[value-4]',`correo`='[value-5]' WHERE 1


# INSERT INTO `profesor`(`id`, `nombre`, `apellido`, `telefono`, `correo`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]')
 
 
            
#testconectar_a_basededatos()          
# consultar_profesor()
# insertar_profesor("Alberto", "Espinoza", "61383453", "mario.com")
# consultar_profesor()
# modificar_profesor(2,"1", "2", "3", "4")
# consultar_profesor()
eliminar_profesor(2)
consultar_profesor()
consultarid_profesor(3)

