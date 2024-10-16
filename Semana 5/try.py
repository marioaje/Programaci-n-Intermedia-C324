# # code
# try:
# # es la seccion donde escribo mis codigos, sentencias, llamados de procedimientos
# #conexiones a base de datos
# resulta = 10/0

# except:
#     print("Error en el sistema.")
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
    
    
    
