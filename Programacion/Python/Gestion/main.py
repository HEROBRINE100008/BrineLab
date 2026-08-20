from create_db import init_db
import add
from show import showTable, showSales, showEarnings
import critic
from update import upd
from register import regis


def menu():
    init_db()

    while True:
        print("""\n-------Gestión de productos-------
        1. Registrar nuevo producto
        2. Ver inventario
        3. Stock crítico
        4. Actualizar stock
        5. Registrar una venta
        6. Historial de ventas
        7. Reporte de ganancias
        8. Salir
        """)

        option = input("elija una opción(1-8): ")

        match option:
            case '1':
                add.add_Product()
            case '2':
                showTable()
            case '3':
                critic.show()
            case '4':
                upd()
            case '5':
                regis()
            case '6':
                showSales()
            case '7':
                showEarnings()
            case '8':
                break


if __name__ == "__main__":
    menu()
