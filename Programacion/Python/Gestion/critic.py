import sqlite3
from show import heading


def show():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM productos WHERE stock <= stock_minimo")

    info = cur.fetchall()

    if not info:
        print("¡Todo está en orden! "
              "No hay productos con stock crítico en este momento.")
    else:
        lineas = heading()
        for fila in info:
            print(
                    f"{fila[0]:<5}{fila[1]:<21}{fila[2]:<17}"
                    f"${fila[4]:<16,.2f}{fila[5]}"
            )
        print(lineas)


if __name__ == "__main__":
    show()
