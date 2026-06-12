from train import data


def menu():
    print("--- Calculadora de Peso Máximo ---")
    while True:
        catalog = data()
        i = 1
        for c in catalog:
            print(f"{i}. {c.name}")
            i += 1


if __name__ == "__main__":
    menu()
