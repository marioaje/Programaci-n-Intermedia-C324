# Ejercicio 1: Diccionario de Calificaciones
# Crea un programa que permita al usuario ingresar los nombres y calificaciones de varios estudiantes, y luego calcula el promedio de las calificaciones.
# Instrucciones:
# El usuario ingresa la cantidad de estudiantes.
# Luego, el usuario ingresa el nombre y la calificación de cada estudiante.
# El programa calcula y muestra el promedio de las calificaciones.
# Código: En archivo separado

 #Diccionario de Calificaciones
califcaciones = {}
 
continuar = "s" 
# Pide al usuario ingresar las calificaciones de los estudiantes que necesite.
numeroestudiantes = 0
while continuar.lower() == "s":
    # Luego, el usuario ingresa el nombre
    nombrecapturado =  input( f"El nombre del estudiante: ")
    
    #a calificación de cada estudiante.
    valorcapturado =  float(input( f"Introduzca la nueva calificacion del estudiante: "))
    califcaciones[nombrecapturado] = valorcapturado
    numeroestudiantes += 1
    continuar = input( "Desea ingresar un nuevo estudiante (s/n)" )


# El promedio de las calificaciones.
promedio = sum(califcaciones.values()) / numeroestudiantes



for item in califcaciones:
    print(item)


for item in califcaciones.values():
    print(item)


# {
#     "key":"values",
#     "Mario": 80
# }



print(califcaciones)
print("El promedio es:", promedio)
print("Cantidad de estudiantes:", numeroestudiantes)

