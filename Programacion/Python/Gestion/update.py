import sqlite3
from show import showTable, showRows, heading


def getInfo(cur, ID):
    cur.execute("SELECT * FROM productos WHERE id = ?", ID)

    info = cur.fetchall()
    return info


def upd():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    update = ("""
            UPDATE productos
            SET stock =  stock + ?
            WHERE id = ?;
            """)

    showTable()

    ID = input("Ingrese el ID del producto a actualizar: ")

    info = getInfo(cur, ID)

    lineas = heading()
    showRows(info)
    print(lineas)

    for row in info:
        oldStock = row[5]

    addStock = input("Ingrese Unidades a añadir: ")
    cur.execute(update, (addStock, ID))
    con.commit()

    info = getInfo(cur, ID)
    for row in info:
        print(f"¡Stock actualizado! '{row[1]}' pasó de {oldStock} a {row[5]}")

    con.close()


if __name__ == "__main__":
    upd()
