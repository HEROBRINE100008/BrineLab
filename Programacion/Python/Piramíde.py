while True:
    opcion = input("1. Empezar programa \n2. salir \n elige una opción: ")
    if opcion == "1":
        blocks = int(input("Ingresa el número de bloques: "))
        height = 0
        layer = 1
        while blocks >= layer:
            blocks -= layer
            height += 1
            layer += 1
        print("La altura de la pirámide:", height)
    if opcion == "2":
        print("Saliendo del programa")
        break