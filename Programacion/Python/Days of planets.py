def marte():
    Valor1 = int(input("introduce soles marcianos: "))
    Resultado = Valor1 * 1.02749125
    print("dias terrestres: ", Resultado)
def mercurio():
    Valor1 = int(input("introduce dias mercurianos: "))
    Resultado = Valor1 * 58.6462
    print("dias terrestres: ", Resultado)
def venus():
    Valor1 = int(input("introduce dias venusianos: "))
    Resultado = Valor1 * 243.0187
    print("dias terrestres: ", Resultado)
def jupiter():
    Valor1 = int(input("introduce dias jovianos: "))
    Resultado = Valor1 * 0.41354
    print("dias terrestres: ", Resultado)
def saturno():
    Valor1 = int(input("introduce dias saturnianos: "))
    Resultado = Valor1 * 0.44401
    print("dias terrestres: ", Resultado)
def urano():
    Valor1 = int(input("introduce dias uranianos: "))
    Resultado = Valor1 * 0.71833
    print("dias terrestres: ", Resultado)
def neptuno():
    Valor1 = int(input("introduce dias neptunianos: "))
    Resultado = Valor1 * 0.67125
    print("dias terrestres: ", Resultado)
def pluton():
    Valor1 = int(input("introduce dias plutonianos: "))
    Resultado = Valor1 * 6.3872
    print("dias terrestres: ", Resultado)
def luna():
    Valor1 = int(input("introduce dias lunarianos: "))
    Resultado = Valor1 * 27.321661
    print("dias terrestres: ", Resultado)
def sol():
    Valor1 = int(input("introduce dias solares: "))
    Resultado = Valor1 * 1
    print("dias terrestres: ", Resultado)
def tierra():
    Valor1 = int(input("introduce dias terrestres: "))
    Resultado = Valor1 * 1
    print("dias terrestres: ", Resultado)
def menu():
    print("1. Marte")
    print("2. Mercurio")
    print("3. Venus")
    print("4. Jupiter")
    print("5. Saturno")
    print("6. Urano")
    print("7. Neptuno")
    print("8. Pluton")
    print("9. Luna")
    print("10. Sol")
    print("11. Tierra")
    print("12. Salir")
    
menu()
while True:
    Operacion = int(input("Elige Una Opción: "))
    
    if Operacion == 1:
        marte()
    elif Operacion == 2:
        mercurio()
    elif Operacion == 3:
        venus()
    elif Operacion == 4:
        jupiter()
    elif Operacion == 5:
        saturno()
    elif Operacion == 6:
        urano()
    elif Operacion == 7:
        neptuno()
    elif Operacion == 8:
        pluton()
    elif Operacion == 9:
        luna()
    elif Operacion == 10:
        sol()
    elif Operacion == 11:
        tierra()
    elif Operacion == 12:
        print("Saliste del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")