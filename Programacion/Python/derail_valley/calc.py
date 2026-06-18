from train import data, srchCatalog


def calcWeight(trainID):
    catalog = data()
    trainFound = srchCatalog(trainID, catalog)
    loadWeight = float(input("Introduzca el peso de la carga: "))

    if trainFound is not None:
        trainFound.maxWeight -= loadWeight

        if trainFound.gotTender is True:
            trainFound.maxWeight -= trainFound.tenderWeight

        if trainFound.maxWeight >= 0:
            print("El peso está en rango de capacidad de carga")
            print(f"Restante: {trainFound.maxWeight}t")

        else:
            print("capacidad de carga sobrepasado por ",
                  f"{trainFound.maxWeight}t")

    else:
        print("Error:Opción no valida")


if __name__ == "__main__":
    print("ya no hay na aqui pai")
