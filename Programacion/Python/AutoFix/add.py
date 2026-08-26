import sqlite3


# Función de registrar los clientes
def regCostumer():
    # Conexión con la base de datos
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()
    # Comando de SQL
    into = ("""
    INSERT INTO cliente
    (ID, nombre_completo, telefono, correo_electronico)
    VALUES(?, ?, ?, ?)
    """)
    # Pidiendo datos del cliente
    ID = input("Introduzca el Documento de identidad(ID/Cédula): ")
    name = input("Introduzca el nombre completo del cliente: ")
    number = input("Introduzca el Numero de Teléfono: ")
    email = input("Introduzca el Correo electrónico: ")

    cur.execute(into, (ID, name, number, email))

    print(f"Cliente {name} registrado correctamente.")

    con.commit()
    con.close()


if __name__ == "__main__":
    option = input("1. Registrar Cliente\n2. Registrar Vehículo\n#: ")
    if option == '1':
        regCostumer()
    elif option == '2':
        print("Coming soon")
