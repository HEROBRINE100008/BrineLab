import calc


def menu():
    option = 0
    while True:
        print("""Selecciona una opción:
              1. °F
              2: °C
              3. K
              4. Salir""")
        
        option = input("Ingrese un numero(1-4): ")
        match option:
            case '1':
                print("""Seleccione una opción
                      1. °F a °C
                      2. °F a K""")
                sub_option = input("Ingrese un número(1-2): ")
                if sub_option == "1":
                    

if __name__ == "__main__":
    menu()

