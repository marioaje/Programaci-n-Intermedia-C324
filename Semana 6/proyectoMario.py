# Objetivo: Desarrollar un sistema simple para administrar una academia que permita gestionar estudiantes, cursos y calificaciones utilizando listas en Python.

# Características del Sistema:

#     Gestión de Estudiantes:
#         Permitir la adición de nuevos estudiantes a la lista de estudiantes.
#         Mostrar la lista de todos los estudiantes registrados.
#         Buscar un estudiante por su nombre y mostrar sus detalles.

#     Gestión de Cursos:
#         Permitir la adición de nuevos cursos a la lista de cursos.
#         Mostrar la lista de todos los cursos ofrecidos por la academia.
#         Permitir a los estudiantes inscribirse en un curso.

#     Gestión de Calificaciones:
#         Permitir la asignación de calificaciones a estudiantes para cada curso.
#         Mostrar las calificaciones de un estudiante específico en todos sus cursos.
#         Calcular el promedio de calificaciones de un estudiante.

# Estructura de Datos:

#     Utilizar listas para almacenar:
#         Estudiantes: cada estudiante será un diccionario con claves como nombre, edad, y cursos (una lista de cursos en los que está inscrito).
#         Cursos: cada curso será un diccionario con claves como nombre y calificaciones (un diccionario donde la clave es el nombre del estudiante y el valor es su calificación).

# Consideraciones:

#     El sistema debe manejar la validación de entradas y los casos en los que un estudiante o curso ya existan.
#     Se pueden agregar más funcionalidades según sea necesario, como la eliminación de estudiantes o cursos.
    
#             Permitir la adición de nuevos estudiantes a la lista de estudiantes.
#         Mostrar la lista de todos los estudiantes registrados.
#         Buscar un estudiante por su nombre y mostrar sus detalles.
        
#         listaestudiantes=[]
#         diccionario {nombre, apellido, cedula}
#         mario jimenez 123
        
#         listacurso = []
#         diccionariocurso ={nombre, categoria, idcurso}
#         python, programacion, 123
        
#         listacalifaciones = []
#         diccionariocalificaciones = {
#             cedula,
#             idcurso,
#             nota
#         }
        
        
#         while, for in
#         usemos funciones
# Listas para almacenar estudiantes y cursos
estudiantes = []
cursos = []

# Función para agregar un estudiante
def agregar_estudiante(id_estudiante, nombre, edad):
    estudiante = {
        'id': id_estudiante,
        'nombre': nombre,
        'edad': edad,
        'cursos': []
    }
    estudiantes.append(estudiante)

# Función para agregar un curso
def agregar_curso(id_curso, nombre):
    curso = {
        'id': id_curso,
        'nombre': nombre,
        'calificaciones': {}
    }
    cursos.append(curso)

# Función para inscribir un estudiante en un curso
def inscribir_estudiante(id_estudiante, id_curso):
    estudiante_encontrado = None
    curso_encontrado = None
    
    # Buscar el estudiante por su ID
    for estudiante in estudiantes:
        if estudiante['id'] == id_estudiante:
            estudiante_encontrado = estudiante
            break

    # Buscar el curso por su ID
    for curso in cursos:
        if curso['id'] == id_curso:
            curso_encontrado = curso
            break
    
    if estudiante_encontrado and curso_encontrado:
        # Inscribir el estudiante al curso usando ID y nombre del curso
        estudiante_encontrado['cursos'].append({
            'id_curso': curso_encontrado['id'],
            'nombre': curso_encontrado['nombre']
        })
        print(f"Estudiante {estudiante_encontrado['nombre']} inscrito en {curso_encontrado['nombre']}")
    else:
        print("Estudiante o curso no encontrado")

# Función para asignar una calificación
def asignar_calificacion(id_estudiante, id_curso, calificacion):
    estudiante_encontrado = None
    curso_encontrado = None
    
    # Buscar el estudiante por su ID
    for estudiante in estudiantes:
        if estudiante['id'] == id_estudiante:
            estudiante_encontrado = estudiante
            break
    
    # Buscar el curso por su ID
    for curso in cursos:
        if curso['id'] == id_curso:
            curso_encontrado = curso
            break
    
    if estudiante_encontrado and curso_encontrado:
        curso_encontrado['calificaciones'][estudiante_encontrado['nombre']] = calificacion
        print(f"Calificación {calificacion} asignada a {estudiante_encontrado['nombre']} en el curso {curso_encontrado['nombre']}")
    else:
        print("Estudiante o curso no encontrado")

# Función para mostrar los estudiantes
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            cursos_estudiante = ", ".join([f"{curso['nombre']} (ID: {curso['id_curso']})" for curso in estudiante['cursos']])
            print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Cursos: {cursos_estudiante}")

# Función para mostrar los cursos
def mostrar_cursos():
    if len(cursos) == 0:
        print("No hay cursos registrados.")
    else:
        for curso in cursos:
            print(f"ID: {curso['id']}, Curso: {curso['nombre']}, Calificaciones: {curso['calificaciones']}")

# Función para mostrar información de un estudiante por su ID
def mostrar_info_estudiante(id_estudiante):
    estudiante_encontrado = None
    
    # Buscar el estudiante por su ID
    for estudiante in estudiantes:
        if estudiante['id'] == id_estudiante:
            estudiante_encontrado = estudiante
            break
    
    if estudiante_encontrado:
        print(f"\n--- Información del Estudiante ---")
        print(f"ID: {estudiante_encontrado['id']}")
        print(f"Nombre: {estudiante_encontrado['nombre']}")
        print(f"Edad: {estudiante_encontrado['edad']}")
        if len(estudiante_encontrado['cursos']) > 0:
            print("Cursos inscritos:")
            for curso in estudiante_encontrado['cursos']:
                # Buscar calificación del curso
                curso_encontrado = None
                for c in cursos:
                    if c['id'] == curso['id_curso']:
                        curso_encontrado = c
                        break
                calificacion = curso_encontrado['calificaciones'].get(estudiante_encontrado['nombre'], "Sin calificación")
                print(f"- {curso['nombre']} (ID: {curso['id_curso']}), Calificación: {calificacion}")
        else:
            print("El estudiante no está inscrito en ningún curso.")
    else:
        print("Estudiante no encontrado.")

# Menú principal
def menu():
    while True:
        print("\n----- Menú Principal -----")
        print("1. Agregar estudiante")
        print("2. Agregar curso")
        print("3. Inscribir estudiante en curso")
        print("4. Asignar calificación a estudiante")
        print("5. Mostrar estudiantes")
        print("6. Mostrar cursos")
        print("7. Salir")
        print("8. Buscar estudiante por ID")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_estudiante = input("ID del estudiante: ")
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            agregar_estudiante(id_estudiante, nombre, edad)
            print(f"Estudiante {nombre} agregado correctamente.")
        
        elif opcion == '2':
            id_curso = input("ID del curso: ")
            nombre_curso = input("Nombre del curso: ")
            agregar_curso(id_curso, nombre_curso)
            print(f"Curso {nombre_curso} agregado correctamente.")
        
        elif opcion == '3':
            id_estudiante = input("ID del estudiante: ")
            id_curso = input("ID del curso: ")
            inscribir_estudiante(id_estudiante, id_curso)
        
        elif opcion == '4':
            id_estudiante = input("ID del estudiante: ")
            id_curso = input("ID del curso: ")
            calificacion = float(input("Calificación: "))
            asignar_calificacion(id_estudiante, id_curso, calificacion)
        
        elif opcion == '5':
            mostrar_estudiantes()
        
        elif opcion == '6':
            mostrar_cursos()
        
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        elif opcion == '8':
            id_estudiante = input("ID del estudiante a buscar: ")
            mostrar_info_estudiante(id_estudiante)
            
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()
