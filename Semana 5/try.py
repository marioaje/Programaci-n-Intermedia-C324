# # code
# try:
# # es la seccion donde escribo mis codigos, sentencias, llamados de procedimientos
# #conexiones a base de datos
# resulta = 10/0
try:
    print(10 / 0)
    # break  # Esta línea causa un error porque no está en un bucle
except ZeroDivisionError:
    print("Se produjo un error de división entre cero...")
except (ValueError, TypeError):
    print("Se produjo un error de valor o tipo...")
except Exception:  # Se debe especificar el tipo de excepción o usar Exception
    print("Se produjo un error desconocido...")

# except:
#     print("Error en el sistema.")
values = [i for i in range(-1, -3, -1)]
print(values)

tuple_state = ("Inactivo", "Activo")
try:    
    resultado = 10/0

    print("El resultado es:", resultado)
except:
    print("Error en el sistema.")
    
print("El sistema no se bug, continuo los procesos")    
# resultado = 10/0
# print("El sistema no se bug, continuo los procesos")    
# print("El resultado es:", resultado)


def suma(x, y):
    return x + y

try:
    x= int(input("Ingrese un numero"))
    y = int(input("Ingrese un numero"))

    #resultado = x + y

    print("El resultado es:", suma(x, y))
except ValueError:
    print("Usted un ingreso algo que no es numero")
except:
    print("Error general")    
    
    
    
