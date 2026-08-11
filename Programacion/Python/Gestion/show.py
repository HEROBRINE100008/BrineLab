import sqlite3


def heading():
    lineas = "=" * 79

    print(lineas)
    print(
            f"{"ID":<5}{"NOMBRE":<21}{"CATEGORÍA":<17}"
            f"{"PRECIO VENTA":<16}{"STOCK"}"
    )
    print(lineas)

    return lineas


def showTable():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM productos")

    info = cur.fetchall()

    lineas = heading()
    for fila in info:
        print(
                f"{fila[0]:<5}{fila[1]:<21}{fila[2]:<17}"
                f"${fila[4]:<16,.2f}{fila[5]}"
        )

    print(lineas)

    con.close()


if __name__ == "__main__":
    showTable()
