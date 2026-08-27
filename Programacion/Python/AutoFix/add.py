# Este es un módulo para añadir clientes y vehículos en la base de datos
import sqlite3


# Función de registrar los clientes
def regCostumer():
    try:
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

        # Ejecutando comando de SQL
        cur.execute(into, (ID, name, number, email))

        # Confirmando registro del cliente
        print(f"Cliente {name} registrado correctamente.")
        input("Presione Enter para continuar...")

        # Guarda los cambios en la base de datos
        con.commit()
    except sqlite3.IntegrityError:
        print("Error: El cliente ya se encuentra registrado.")
    finally:
        # Cerrando conexión con la base de datos
        con.close()


# Esto es solo para probar la función fuera del main
if __name__ == "__main__":
    option = input("1. Registrar Cliente\n2. Registrar Vehículo\n#: ")
    if option == '1':
        regCostumer()
    elif option == '2':
        print("Coming soon")
