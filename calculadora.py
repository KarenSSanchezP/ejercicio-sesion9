import producto
import suma
import resta

def calculadora(operacion, numero1, numero2):
    if operacion == '1':
        return suma.suma(numero1, numero2)
    elif operacion == '2':
        return resta.resta(numero1, numero2)
    elif operacion == '3':
        return producto.producto(numero1, numero2)

operacion = input("Ingrese la operación (1-suma, 2-resta, 3-multiplicacion): ")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
resultado = calculadora(operacion, numero1, numero2)
print(f"El resultado de la operación {operacion} es {resultado}")