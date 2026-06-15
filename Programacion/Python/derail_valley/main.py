from train import data

def lista()


def menu():
    print("--- Calculadora de Peso Máximo ---")
    while True:
        catalog = data()
        i = 1
        for c in catalog:
            print(f"{i}. {c.name}")
            i += 1
        
        option = int(input("Elija un numero: "))



if __name__ == "__main__":
    menu()
