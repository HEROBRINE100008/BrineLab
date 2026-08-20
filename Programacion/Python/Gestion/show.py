import sqlite3


def heading():
    lineas = "=" * 98

    print(lineas)
    print(
            f"{"ID":<5}{"NOMBRE":<40}{"CATEGORÍA":<17}"
            f"{"PRECIO VENTA":<16}{"STOCK"}"
    )
    print(lineas)

    return lineas


def showRows(row):
    for fila in row:
        print(
                f"{fila[0]:<5}{fila[1]:<40}{fila[2]:<17}"
                f"${fila[4]:<16,.2f}{fila[5]}"
        )


def showEarnings():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("""
                SELECT
                COUNT(*) AS ventas_registradas,
                COALESCE(SUM(v.total), 0) AS total_ingresos,
                COALESCE(SUM(v.cantidad * p.precio_costo), 0) AS costo_total,
                COALESCE(SUM(v.total) - SUM(v.cantidad * p.precio_costo), 0)
                AS ganancia_neta
                FROM ventas AS v
                JOIN productos AS p ON v.producto_id = p.id;
                """)

    ventas, ingresos, costo, ganancia = cur.fetchone()

    rows = "=" * 48
    row = "-" * 48

    print(f"""
          {rows}
          {'REPORTE FINANCIERO GENERAL':^48}
          {rows}
          {'Total Ventas Registradas:':<28}{ventas:<20}
          {'Total Ingresos:':<28}{ingresos:<20,.2f}
          {'Costo de Inversión:':<28}{costo:<20,.2f}
          {row}
          {'GANANCIA NETA ESTIMADA:':<28}{ganancia:<20,.2f}
          {rows}
          """)

    con.commit()


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

    lines = "=" * 95

    print(lines)
    print(
        f"{'ID VENTA':<10}{'FECHA / HORA':<21}{'PRODUCTO':<30}"
        f"{'CANT.':<7}{'PRECIO UNIT.':<14}{'TOTAL':<13}"
        )
    print(lines)
    for row in info:
        print(
                f"{row[0]:<10}{row[1]:<21}{row[2]:<30}"
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
