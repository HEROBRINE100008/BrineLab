#-------------------------------------
#Ejercicio: Aula_28_Diciembre_15_sql.py
#Ejecución.
#Bajo consola linux.
#python3 Aula_28_Diciembre_15_sql.py
#************************************
import sqlite3
 
# Función para inicializar la base de datos
def inicializar_db():
    conexion = sqlite3.connect("Aula_28_Agenda.db")
    cursor = conexion.cursor()
    # Crear la tabla de contactos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            ciudad TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()
 
# Función para agregar un contacto
def agregar_contacto(nombre, telefono, ciudad):
    conexion = sqlite3.connect("Aula_28_Agenda.db")
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO contactos (nombre, telefono, ciudad) VALUES (?, ?, ?)",
        (nombre, telefono, ciudad)
    )
    conexion.commit()
    conexion.close()
    print(f"Contacto '{nombre}' agregado exitosamente.")
 
# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    conexion = sqlite3.connect("Aula_28_Agenda.db")
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT nombre, telefono, ciudad FROM contactos WHERE nombre LIKE ?",
        (f"%{nombre}%",)
    )
    resultados = cursor.fetchall()
    conexion.close()
 
    if resultados:
        print("\nContactos encontrados:")
        for contacto in resultados:
            print(f"- {contacto[0]}: {contacto[1]} (Ciudad: {contacto[2]})")
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")
 
# Función para eliminar un contacto por nombre
def eliminar_contacto(nombre):
    conexion = sqlite3.connect("Aula_28_Agenda.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM contactos WHERE nombre LIKE ?", (f"%{nombre}%",))
    cambios = cursor.rowcount
    conexion.commit()
    conexion.close()
 
    if cambios > 0:
        print(f"Contacto(s) con el nombre '{nombre}' eliminado(s).")
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")
 
# Función para mostrar todos los contactos
def mostrar_agenda():
    conexion = sqlite3.connect("Aula_28_Agenda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, telefono, ciudad FROM contactos")
    contactos = cursor.fetchall()
    conexion.close()
 
    if contactos:
        print("\nContactos en la agenda:")
        for contacto in contactos:
            print(f"- {contacto[0]}: {contacto[1]} (Ciudad: {contacto[2]})")
    else:
        print("La agenda está vacía.")
 
# Función principal para el menú
def menu():
    inicializar_db()  # Asegurar que la base de datos esté lista antes de usarla
 
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
 
        opcion = input("Elige una opción: ")
 
        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            ciudad = input("Ciudad del contacto: ")
            agregar_contacto(nombre, telefono, ciudad)
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "4":
            mostrar_agenda()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
 
# Ejecutar el programa
menu()