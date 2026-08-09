import sqlite3


def init_db():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "productos" (
        "id"    INTEGER NOT NULL UNIQUE,
        "nombre"    TEXT NOT NULL,
        "precio_costo"  INTEGER NOT NULL,
        "stock" INTEGER NOT NULL,
        "stock_minimo"  INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
    )""")
    return 1


if __name__ == "__main__":
    print(init_db())
