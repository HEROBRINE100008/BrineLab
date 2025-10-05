#Selección de temperatura
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

        opcion2= input("Ingresa el número de tu elección: ")
        if opcion2 == "1":
            Farenheit = int(input("Cual es la temperatura a convertir? "))
            Celsius = (Farenheit - 32) * 5 / 9
            print(Celsius, "°C")
        elif opcion2 == "2":
            Farenheit = int(input("Cual es la temperatura a convertir? "))
            Kelvin = (Farenheit - 32) * 5 / 9 + 273.15
            print(Kelvin,"K")
    elif opcion == "2":
        print("Selecciona una opción:")
        print("1. °C a °F")
        print("2. °C a K")

        opcion3= input("Ingresa el número de tu elección: ")
        if opcion3 == "1":
            Celsius = int(input("Cual es la temperatura a convertir? "))
            Farenheit = (Celsius * 9/5) + 32
            print(Farenheit, "°F")
        elif opcion3 == "2":
            Celsius = int(input("Cual es la temperatura a convertir? "))
            Kelvin = Celsius + 273.15
            print(Kelvin,"K")
    elif opcion == "3":
        print("Selecciona una opción:")
        print("1. K a °F")
        print("2. K a °C")

        opcion4= input("Ingresa el número de tu elección: ")
        if opcion4 == "1":
            Kelvin = int(input("Cual es la temperatura a convertir? "))
            Farenheit = (Kelvin - 273.15) * 9/5 + 32
            print(Farenheit, "°F")
        elif opcion4 == "2":
            Kelvin = int(input("Cual es la temperatura a convertir? "))
            Celsius = Kelvin - 273.15
            print(Celsius,"°C")
    elif opcion == "4":
         print("Saliendo del programa.")
         break
        
    
    else:
                    print("Opción inválida. Por favor, intenta nuevamente.")
