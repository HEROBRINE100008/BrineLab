#Calculadora Simple v2
    
#Suma

def suma():
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 + Valor2
    print("Tu resultado es: ", Resultado)

#Resta

def resta():
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 - Valor2
    print("Tu resultado es: ", Resultado)

#Multiplicación

def multiplicación():
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 * Valor2
    print("Tu resultado es: ", Resultado)

#División

def división():
    Valor1 = int(input("Dame el primer valor: "))
    Valor2 = int(input("Dame el segundo valor: "))
    Resultado = Valor1 / Valor2
    print("Tu resultado es: ", Resultado)

#Menú
Operacion = 0

#Pregunta al usuario que tipo de operación quiere hacer

while True:
    
    Operacion = int(input("Elige Una Opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Salir: "))
    
    if Operacion == 1:
          suma()
    
    elif Operacion == 2:
          resta()
    
    elif Operacion == 3:
          multiplicación()
    
    elif Operacion == 4:
          división()
    
    elif Operacion == 5:
        print("Saliste del programa.")
        break
