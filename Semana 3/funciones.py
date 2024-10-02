def nombredelafuncion(parametros):
    operacion = parametros + 1
    return operacion

def sumar ( a, b):
    operacion = a + b
    return operacion

def restar ( a, b):
    operacion = a - b
    return operacion

def multiplicar ( a, b):
    operacion = a * b
    return operacion

def mensaje():
    return "Bienvenidos al curso con el Prof Mario"


####Fin de funciones##########

print(mensaje())


resultado = nombredelafuncion(90)
print(resultado)

print("a=3 b=4")
calculos = sumar(3,4)
print(calculos)

calculos = restar(3,4)
print(calculos)



calculos = multiplicar(3,4)
print(calculos)
