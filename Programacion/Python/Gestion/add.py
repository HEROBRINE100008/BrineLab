import sqlite3


def add_Product():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    into = ("""
    INSERT INTO productos
    (nombre, categoria, precio_costo, precio_venta, stock)
    VALUES(?, ?, ?, ?, ?)
    """)

    name = input("Introduzca el nombre del producto: ")
    category = input("Introduzca la categoria: ")
    priceCost = input("Introduzca costo del producto: ")
    priceSell = input("Introduzca el precio de venta: ")
    stock = input("Introduzca cuanto stock hay: ")

    cur.execute(into, (name, category, priceCost, priceSell, stock))

    con.commit()
    con.close()


if __name__ == "__main__":
    add_Product()
