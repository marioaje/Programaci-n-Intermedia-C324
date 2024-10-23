try:
    print(10 / 0)
    # break  # Esta línea causa un error porque no está en un bucle
except ZeroDivisionError:
    print("Se produjo un error de división entre cero...")
except (ValueError, TypeError):
    print("Se produjo un error de valor o tipo...")
except Exception:  # Se debe especificar el tipo de excepción o usar Exception
    print("Se produjo un error desconocido...")
