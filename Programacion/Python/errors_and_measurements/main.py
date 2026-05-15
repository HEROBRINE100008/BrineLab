from absolute_error import abse


def init():
    lista = []
    continuar = True
    while continuar:
        entrada = float(input("Introduzca una medición: "))
        lista.append(entrada)

        opcion = input("Desea añadir? (s/n): ")
        if opcion.lower() != "s":
            continuar = False

    abse(lista)


if __name__ == "__main__":
    init()
