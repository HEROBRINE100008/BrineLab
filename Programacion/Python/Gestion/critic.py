import sqlite3
from show import heading, showRows


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
        showRows(info)
        print(lineas)

    con.close()


if __name__ == "__main__":
    show()
