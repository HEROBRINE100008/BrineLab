from create_db import init_db
import add


# Función del menu principal
def menu():
    # Esta función crea la base de datos si no existe
    init_db()

    # Aqui se declara la variable para las lineas de el titulo del programa
    row = "-" * 10

    # Bucle para el menú principal
    while True:
        # Interfaz del menú
        print(f"""
        {row}AutoFix{row}
        1. Registrar nuevo cliente
        2. Registrar nuevo vehículo
        3. Buscar cliente
        4. Buscar vehículo
        0. Salir del sistema
        """)

        # Le pide al usuario que introduzca la opción a elegir
        option = int(input("Elija una opcion: "))

        # Evaluamos la entrada del usuario
        match option:

            # Registrar nuevo cliente
            case 1:
                add.regCostumer()
            # Registrar nuevo vehículo
            case 2:
                print("Coming soon...")
            # Buscar cliente
            case 3:
                print("Coming soon...")
            # Buscar vehículo
            case 4:
                print("Coming soon...")
            # Salir
            case 0:
                break


if __name__ == "__main__":
    menu()
