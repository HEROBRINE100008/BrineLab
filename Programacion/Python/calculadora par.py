# Solicitar al usuario que introduzca un número
while True:
    opcion = input("1. Entrar 2.Salir: ")
    if opcion == "1":
        numero = int(input("Introduce un número: "))
        if numero % 2 != 0:
            print(f"El número {numero} es impar.")
        else:
            print(f"El número {numero} es par.")
    else:
        print("Saliendo del programa...")
        break