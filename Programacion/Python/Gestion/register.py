import sqlite3
from update import getInfo
from show import showTable, heading, showRows


def regis():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    showTable()

    regis = ("""
            INSERT INTO ventas
            (producto_id, cantidad, precio_unitario, total)
            VALUES(?, ?, ?, ?)
             """)

    update = ("""
            UPDATE productos
            SET stock = stock - ?
            WHERE id = ?
           """)

    while True:
        ID = input("Ingrese el ID del producto: ")

        info = getInfo(cur, ID)

        if not info:
            print("Error: Producto no existe en la base de datos")
            err = input('Ingrese "S" para reintentar o nada para cancelar: ')
            if err.lower() != "s":
                break
            else:
                continue
        else:
            lineas = heading()
            showRows(info)
            print(lineas)

            for row in info:
                price = row[4]
                stock = row[5]

            units = float(input("Cuantas unidades se venderán: "))

            total = price * units

            res = stock - units

            cur.execute(regis, (ID, units, price, total))

            cur.execute(update, (units, ID))

            lines = "=" * 40
            line = "-" * 40

            for row in info:
                print(f"""
                    {lines}
                    {'COMPROBANTE DE VENTA':^40}
                    {lines}
                    {'Producto:':<18}{row[1]:<23}
                    {'Cantidad:':<18}{units:<23}
                    {'Precio Unitario:':<18}${row[4]:<23,.2f}
                    {'Total A Cobrar:':<18}${total:<23,.2f}
                    {line}
                    {'Stock restante:':<18}{res:<23}
                    {lines}
                    {'¡Venta registrada con éxito!':<}
                """)

            con.commit()
            con.close()
            break


if __name__ == "__main__":
    regis()
