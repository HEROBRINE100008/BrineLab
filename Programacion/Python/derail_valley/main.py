from train import data


def srchCatalog(trainId, trainList):
    for t in trainList:
        if t.ID == trainId:
            return t


def menu():
    print("--- Calculadora de Peso Máximo ---")
    while True:
        catalog = data()
        i = 1
        for c in catalog:
            print(f"{i}. {c.name}")
            i += 1

        option = int(input("Elija un numero: "))
        trainFound = srchCatalog(option, catalog)
        print(f"La Locomotora es la: {trainFound.name}")


if __name__ == "__main__":
    menu()
