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

def main():
    while True:
        opcion = menu()
        if opcion == "1":
            numeros = list(map(float, input("Ingrese los números separados por espacio: ").split()))
            print(f"Resultado: {sumar(*numeros)}")
        elif opcion == "2":
            a, b = map(float, input("Ingrese los dos números separados por espacio: ").split())
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
            a, b = map(float, input("Ingrese los dos números separados por espacio: ").split())
            print(f"Resultado: {dividir(a, b)}")
        elif opcion == "4":
            a, b = map(float, input("Ingrese los dos números separados por espacio: ").split())
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == "5":
            total = float(input("Ingrese el número base: "))
            porcentaje = float(input("Ingrese el porcentaje: "))
            print(f"Resultado: {encontrar_porcentaje(total, porcentaje)}")
        elif opcion == "6":
            a, b = map(float, input("Ingrese los dos números separados por espacio: ").split())
            print(f"Resultado: {encontrar_resto(a, b)}")
        elif opcion == "7":
            a, b = map(float, input("Ingrese los dos números separados por espacio: ").split())
            print(f"Resultado: {parte_entera_division(a, b)}")
        elif opcion == "8":
            numero = int(input("Ingrese un número: "))
            print(f"¿Es primo? {'Sí' if es_primo(numero) else 'No'}")
        elif opcion == "9":
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
