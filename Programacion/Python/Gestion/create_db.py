import sqlite3


def init_db():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "productos" (
        "id"    INTEGER NOT NULL UNIQUE,
        "nombre"    TEXT NOT NULL,
        "categoria" TEXT NOT NULL,
        "precio_costo"  REAL NOT NULL,
        "precio_venta"  REAL NOT NULL,
        "stock" INTEGER NOT NULL,
        "stock_minimo"  INTEGER DEFAULT 5,
        PRIMARY KEY("id" AUTOINCREMENT)
    )""")
    con.commit()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "ventas" (
        "id"    INTEGER NOT NULL UNIQUE,
        "producto_id"   INTEGER,
        "cantidad"  INTEGER,
        "precio_unitario"   INTEGER,
        "total" INTEGER,
        "fecha_hora"    TEXT DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY("id" AUTOINCREMENT),
        FOREIGN KEY("producto_id") REFERENCES "productos"("id")
    )""")
    con.commit()
    con.close()


if __name__ == "__main__":
    init_db()

    print("base de datos creada con exito")
