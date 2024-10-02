# Ejercicio 1: Lista de Calificaciones
# Crea un programa que pida al usuario introducir las calificaciones de varios estudiantes, las almacene en una lista, y luego muestre el promedio, la calificación más alta y la más baja.

# Instrucciones:
# Pide al usuario ingresar las calificaciones de 5 estudiantes.
# Almacena esas calificaciones en una lista.
# Calcula y muestra:
# El promedio de las calificaciones.
# La calificación más alta.
# La calificación más baja.


#Lista de Calificaciones
calificaciones = []

# Pide al usuario ingresar las calificaciones de 5 estudiantes.
for i in range(5):    
    valorcapturado =  float(input( f"Introduzca la nueva calificacion del estudiante: { i + 1 }: "))
    calificaciones.append(valorcapturado)
    
# Calcula y muestra:
# El promedio de las calificaciones.
# La calificación más alta.
# La calificación más baja.
print (calificaciones)

# El promedio de las calificaciones.
promedio = sum(calificaciones) / len(calificaciones)
print (f"El promedio: {promedio}")
# La calificación más alta.
calificacion_maxima = max(calificaciones)
print (f"La calificación más alta: {calificacion_maxima}")
# La calificación más baja.
calificacion_minima = min(calificaciones)
print (f"La calificación más baja: {calificacion_minima}")