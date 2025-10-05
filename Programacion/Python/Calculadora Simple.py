#Calculadora Simple
Operacion = 0
#Pregunta al usuario que tipo de operación quiere hacer 
while True:
    Operacion = int(input("Elige Una Opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Salir: "))
#Suma
    if Operacion == 1:
        Valor1 = int(input("Dame el primer valor: "))
        Valor2 = int(input("Dame el segundo valor: "))
        Resultado = Valor1 + Valor2
        print("Tu resultado es: ", Resultado)
#Resta
    elif Operacion == 2:
        Valor1 = int(input("Dame el primer valor: "))
        Valor2 = int(input("Dame el segundo valor: "))
        Resultado = Valor1 - Valor2
        print("Tu resultado es: ", Resultado)
#Multiplicación
    elif Operacion == 3:
        Valor1 = int(input("Dame el primer valor: "))
        Valor2 = int(input("Dame el segundo valor: "))
        Resultado = Valor1 * Valor2
        print("Tu resultado es: ", Resultado)
#División
    elif Operacion == 4:
        Valor1 = int(input("Dame el primer valor: "))
        Valor2 = int(input("Dame el segundo valor: "))
        Resultado = Valor1 / Valor2
        print("Tu resultado es: ", Resultado)
    elif Operacion == 5:
        print("Saliste del programa.")
        break