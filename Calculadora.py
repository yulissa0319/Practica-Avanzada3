#inicializacion de del proyecto
#Funciones matematicas


# calculadora.py
# Proyecto Avanzado 3: Calculadora Matemática.

def sumar(*numeros):
    return sum(numeros)

def restar(a, b):
    return a - b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."

def multiplicar(a, b):
    return a * b

def encontrar_porcentaje(total, porcentaje):
    return (total * porcentaje) / 100

def encontrar_resto(a, b):
    return a % b

def parte_entera_division(a, b):
    return a // b

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def menu():
    print("\n--- Calculadora Matemática Avanzada ---")
    print("1. Sumar números")
    print("2. Restar números")
    print("3. Dividir números")
    print("4. Multiplicar números")
    print("5. Encontrar porcentaje de un número")
    print("6. Encontrar resto de una división")
    print("7. Encontrar parte entera de una división")
    print("8. Verificar si un número es primo")
    print("9. Salir")

    opcion = input("\nSeleccione una opción: ")
    return opcion


