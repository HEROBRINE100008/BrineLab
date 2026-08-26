def menu():
    row = "-" * 10
    while True:
        print(f"""
        {row}AutoFix{row}
        1. Registrar nuevo cliente
        2. Registrar nuevo vehículo
        3. Buscar cliente
        4. Buscar vehículo
        5. Salir del sistema
        """)

        option = int(input("Elija una opcion: "))

        match option:

            case 1:
                
            case 5:
                break


if __name__ == "__main__":
    menu()
