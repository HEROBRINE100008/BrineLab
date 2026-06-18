class Train:
    def __init__(self, ID, name, weight, tenderWeight, maxWeight, gotTender):
        self.ID = ID
        self.name = name
        self.weight = weight
        self.tenderWeight = tenderWeight
        self.maxWeight = maxWeight
        self.gotTender = gotTender


def data():
    Catalog = [
        Train(1, "DE2", 38.0, 0.0, 250.0, False),
        Train(2, "S060", 50.7, 0.0, 300.0, False),
        Train(3, "DM3", 52.0, 0.0, 400.0, False),
        Train(4, "DH4", 77.5, 0.0, 500.0, False),
        Train(5, "S282", 124.8, 50.0, 800.0, True),
        Train(6, "DE6", 125.0, 0.0, 1000.0, False)
    ]
    return Catalog


def srchCatalog(trainId, trainList):
    for t in trainList:
        if t.ID == trainId:
            return t


if __name__ == "__main__":
    catalog = data()
    print("ID\tNombre\tPeso")
    for c in catalog:
        print(f"{c.ID}\t{c.name}\t{c.weight}")
