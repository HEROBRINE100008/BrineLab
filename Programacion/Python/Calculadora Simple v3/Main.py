from calculadora import suma, resta, multiplicación, división

#Menú
Operacion = 0

#Pregunta al usuario que tipo de operación quiere hacer

while True:
    
    Operacion = int(input("Elige Una Opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Salir: "))
    
    if Operacion == 1:
          v1 = int(input("Dame el primer valor: "))
          v2 = int(input("Dame el segundo valor: "))
          print("Tu resultado es: ",suma(v1,v2))
    
    elif Operacion == 2:
          v1 = int(input("Dame el primer valor: "))
          v2 = int(input("Dame el segundo valor: "))
          print("Tu resultado es: ",resta(v1,v2))
    
    elif Operacion == 3:
          v1 = int(input("Dame el primer valor: "))
          v2 = int(input("Dame el segundo valor: "))
          print("Tu resultado es: ",multiplicación(v1,v2))
    
    elif Operacion == 4:
          v1 = int(input("Dame el primer valor: "))
          v2 = int(input("Dame el segundo valor: "))
          print("Tu resultado es: ",división(v1,v2))
    
    elif Operacion == 5:
        print("Saliste del programa.")
        break
