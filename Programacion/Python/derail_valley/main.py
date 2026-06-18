from train import data
from calc import calcWeight


def menu():
    print("--- Calculadora de Peso Máximo ---")
    while True:
        catalog = data()
        i = 1
        for c in catalog:
            print(f"{i}. {c.name}")
            i += 1

        print("7. Salir")
        option = int(input("Elija un numero: "))

        if option <= 6:
            calcWeight(option)
        else:
            break


if __name__ == "__main__":
    menu()
