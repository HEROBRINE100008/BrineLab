import sqlite3


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

for row in info:
    print(row)
