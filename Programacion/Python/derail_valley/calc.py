from train import data
from main import srchCatalog


def calcWeight(trainId, trainList):
    for t in trainList:
        if t.ID == trainId:
            return t


if __name__ == "__main__":
    catalog = data()
    trainID = 2

    trainFound = srchCatalog(trainID, catalog)
    loadWeight = 200

    if trainFound is not None:
        trainFound.maxWeight -= loadWeight

        if trainFound.maxWeight >= 0:
            print("El peso está en rango de capacidad de carga")
            print(f"Restante: {trainFound.maxWeight}t")
        else:
            print(f"capacidad de carga sobrepasado por {}")

    else:
        print("Error:Objeto Nulo")
