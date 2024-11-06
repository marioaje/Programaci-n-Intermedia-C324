# menu.py
import funcionesinventario

def mostrar_menu():
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))
            funcionesinventario.agregar_producto(id_producto, nombre, precio, cantidad)
        elif opcion == "2":
            id_producto = input("ID del producto a consultar: ")
            funcionesinventario.consultar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = int(input("Nueva cantidad en stock: "))
            funcionesinventario.actualizar_stock(id_producto, nueva_cantidad)
        elif opcion == "4":
            id_producto = input("ID del producto a eliminar: ")
            funcionesinventario.eliminar_producto(id_producto)
        elif opcion == "5":
            funcionesinventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
