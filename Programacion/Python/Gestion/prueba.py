import sqlite3
from update import getInfo

con = sqlite3.connect("Sql.db")
cur = con.cursor()

ID = input("id: ")

info = getInfo(cur, ID)

lines = "=" * 40
line = "-" * 40

units = 5

total = 0

for row in info:
    total = row[4] * units

    res = row[5] - units

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
