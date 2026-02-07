from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# ================= CONFIG EMAIL =================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMITENTE = "ismael011913@gmail.com"
EMAIL_PASSWORD = "hvhuowysbcoohkta"

# ===============================================

# ---------- DB ----------
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
            email TEXT NOT NULL,
            monto REAL NOT NULL,
            plan_dias INTEGER NOT NULL,
            inicio DATE NOT NULL,
            vencimiento DATE NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS facturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            nombre TEXT,
            email TEXT,
            monto REAL,
            fecha DATE
        )
    """)

    conn.commit()
    conn.close()

# ---------- LIMPIEZA ----------
def limpiar_clientes_vencidos():
    hoy = datetime.now().date()
    limite = hoy - timedelta(days=30)

    conn = get_db()
    conn.execute("DELETE FROM clientes WHERE vencimiento < ?", (limite,))
    conn.commit()
    conn.close()

# ---------- ENVÍO DE FACTURA ----------
def enviar_factura_email(nombre, email, monto, fecha):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Factura de tu membresía - GYM Manager"
    msg["From"] = EMAIL_REMITENTE
    msg["To"] = email

    html = render_template(
        "factura_email.html",
        nombre=nombre,
        monto=monto,
        fecha=fecha
    )

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_REMITENTE, EMAIL_PASSWORD)
        server.sendmail(EMAIL_REMITENTE, email, msg.as_string())

# ---------- RUTAS ----------
@app.route("/")
def index():
    limpiar_clientes_vencidos()

    conn = get_db()
    clientes = conn.execute("SELECT * FROM clientes ORDER BY id DESC").fetchall()
    conn.close()

    hoy = datetime.now().date().isoformat()
    return render_template("index.html", clientes=clientes, hoy=hoy)

@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["name"]
    email = request.form["email"]
    monto = float(request.form["monto"])
    plan_dias = int(request.form["plan"])
    inicio = datetime.strptime(request.form["startDate"], "%Y-%m-%d").date()
    vencimiento = inicio + timedelta(days=plan_dias)

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO clientes (nombre, email, monto, plan_dias, inicio, vencimiento)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, email, monto, plan_dias, inicio, vencimiento))

    cliente_id = cur.lastrowid

    cur.execute("""
        INSERT INTO facturas (cliente_id, nombre, email, monto, fecha)
        VALUES (?, ?, ?, ?, ?)
    """, (cliente_id, nombre, email, monto, inicio))

    conn.commit()
    conn.close()

    # 👉 ENVIAR FACTURA POR EMAIL
    enviar_factura_email(nombre, email, monto, inicio)

    return redirect(url_for("factura", id=cliente_id))

@app.route("/factura/<int:id>")
def factura(id):
    conn = get_db()
    factura = conn.execute(
        "SELECT * FROM facturas WHERE cliente_id = ?", (id,)
    ).fetchone()
    conn.close()

    return render_template("factura.html", factura=factura)

# ---------- MAIN ----------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
