#Selección de temperatura

def F_a_C():
    Farenheit = int(input("Cual es la temperatura a convertir? "))
    Celsius = (Farenheit - 32) * 5 / 9
    print(Celsius, "°C")

def F_a_K():
    Farenheit = int(input("Cual es la temperatura a convertir? "))
    Kelvin = (Farenheit - 32) * 5 / 9 + 273.15
    print(Kelvin,"K")

def C_a_F():
    Celsius = int(input("Cual es la temperatura a convertir? "))
    Farenheit = (Celsius * 9/5) + 32
    print(Farenheit, "°F")
    
def C_a_K():
    Celsius = int(input("Cual es la temperatura a convertir? "))
    Kelvin = Celsius + 273.15
    print(Kelvin,"K")

def K_a_F():
    Kelvin = int(input("Cual es la temperatura a convertir? "))
    Farenheit = (Kelvin - 273.15) * 9/5 + 32
    print(Farenheit, "°F")

def K_a_C():
    Kelvin = int(input("Cual es la temperatura a convertir? "))
    Celsius = Kelvin - 273.15
    print(Celsius,"°C")

while True:
    print("Selecciona una opción:")
    print("1. °F")
    print("2. °C")
    print("3. K")
    print("4. Salir")

    opcion = input("Ingresa el número de tu elección: ")
    if opcion == "1":
        print("Selecciona una opción:")
        print("1. °F a °C")
        print("2. °F a K")

        opcion2 = input("Ingresa el número de tu elección: ")
        if opcion2 == "1":
            F_a_C()

        elif opcion2 == "2":
            F_a_K()

    elif opcion == "2":
        print("Selecciona una opción:")
        print("1. °C a °F")
        print("2. °C a K")

        opcion3= input("Ingresa el número de tu elección: ")
        if opcion3 == "1":
            C_a_F()
        elif opcion3 == "2":
            C_a_K()

    elif opcion == "3":
        print("Selecciona una opción:")
        print("1. K a °F")
        print("2. K a °C")

        opcion4= input("Ingresa el número de tu elección: ")
        
        if opcion4 == "1":
            K_a_F()
            
        elif opcion4 == "2":
            K_a_C()

    elif opcion == "4":
         print("Saliendo del programa.")
         break
        
    
    else:
                    print("Opción inválida. Por favor, intenta nuevamente.")
