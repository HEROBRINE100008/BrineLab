from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# =====================
# BASE DE DATOS
# =====================
def get_db():
    conn = sqlite3.connect("gym.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        monto REAL NOT NULL,
        plan_dias INTEGER NOT NULL,
        inicio DATE NOT NULL,
        vencimiento DATE NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# =====================
# LIMPIEZA AUTOMÁTICA
# =====================
def limpiar_clientes_vencidos():
    hoy = datetime.now().date()
    limite = hoy - timedelta(days=30)

    conn = get_db()
    conn.execute(
        "DELETE FROM clientes WHERE vencimiento < ?",
        (limite,)
    )
    conn.commit()
    conn.close()

# =====================
# RUTAS
# =====================
@app.route("/")
def index():
    limpiar_clientes_vencidos()

    conn = get_db()
    clientes = conn.execute(
        "SELECT * FROM clientes ORDER BY id DESC"
    ).fetchall()
    conn.close()

    hoy = datetime.now().date()
    return render_template("index.html", clientes=clientes, hoy=hoy)

@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["name"]
    telefono = request.form["phone"]
    monto = float(request.form["monto"])
    plan_dias = int(request.form["plan"])
    inicio = datetime.strptime(request.form["startDate"], "%Y-%m-%d").date()
    vencimiento = inicio + timedelta(days=plan_dias)

    conn = get_db()
    conn.execute("""
        INSERT INTO clientes (nombre, telefono, monto, plan_dias, inicio, vencimiento)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, telefono, monto, plan_dias, inicio, vencimiento))
    conn.commit()
    conn.close()

    return redirect("/")

# =====================
# INICIO
# =====================
if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8080)
