import sqlite3


con = sqlite3.connect("Sql.db")
cur = con.cursor()

cur.execute("""
            SELECT
            COALESCE(SUM(v.total), 0) AS total_ingresos,
            COALESCE(SUM(v.cantidad * p.precio_costo), 0) AS costo_total,
            COALESCE(SUM(v.total) - SUM(v.cantidad * p.precio_costo), 0) AS ganancia_neta
            FROM ventas AS v
            JOIN productos AS p ON v.producto_id = p.id;
            """)

ingresos, costo, ganancia = cur.fetchone()

rows = "=" * 48
row = "-" * 48

print(f"""
      {rows}
      {'REPORTE FINANCIERO GENERAL':^48}
      {rows}
      {'Total Ventas Registradas:':<28}{'1':<20}
      {'Total Ingresos:':<28}{ingresos:<20,.2f}
      {'Costo de Inversión:':<28}{costo:<20,.2f}
      {row}
      {'GANANCIA NETA ESTIMADA:':<28}{ganancia:<20,.2f}
      {rows}
      """)
