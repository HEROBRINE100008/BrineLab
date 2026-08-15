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


def showRows(row):
    for fila in row:
        print(
                f"{fila[0]:<5}{fila[1]:<21}{fila[2]:<17}"
                f"${fila[4]:<16,.2f}{fila[5]}"
        )


def showSales():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("""
                SELECT
                v.id,
                v.fecha_hora,
                p.nombre,
                v.cantidad,
                v.precio_unitario,
                v.total
                FROM ventas AS v
                INNER JOIN productos AS p
                ON v.producto_id = p.id
                """)

    info = cur.fetchall()

    lines = "=" * 84

    print(lines)
    print(
        f"{'ID VENTA':<10}{'FECHA / HORA':<21}{'PRODUCTO':<19}"
        f"{'CANT.':<7}{'PRECIO UNIT.':<14}{'TOTAL':<13}"
        )
    print(lines)
    for row in info:
        print(
                f"{row[0]:<10}{row[1]:<21}{row[2]:<19}"
                f"{row[3]:<7}{row[4]:<14}{row[5]:<13}"
                )
        print(lines)

        con.close()


def showTable():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM productos")

    info = cur.fetchall()

    lineas = heading()
    showRows(info)
    print(lineas)

    con.close()


if __name__ == "__main__":
    showTable()
    showSales()
