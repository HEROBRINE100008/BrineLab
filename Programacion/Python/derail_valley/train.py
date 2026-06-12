class Train:
    def __init__(self, name, weight, tenderWeight, maxWeight, gotTender):
        self.name = name
        self.weight = weight
        self.tenderWeight = tenderWeight
        self.maxWeight = maxWeight
        self.gotTender = gotTender


def data():
    Catalog = [
        Train("DE2", 38.0, 0.0, 250.0, False),
        Train("S060", 50.7, 0.0, 300.0, False),
        Train("DM3", 52.0, 0.0, 400.0, False),
        Train("DH4", 77.5, 0.0, 500.0, False),
        Train("S282", 124.8, 50.0, 800.0, True),
        Train("DE6", 125.0, 0.0, 1000.0, False)
    ]
    return Catalog


if __name__ == "__main__":
    catalog = data()
    print("Nombre\tPeso")
    for c in catalog:
        print(f"{c.name}\t{c.weight}")
