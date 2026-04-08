import sqlite3
from show import show_Grades
from add import add_Stu
def init_db():
	con = sqlite3.connect("Sql.db")
	cur = con.cursor()

	cur.execute("""
	CREATE TABLE IF NOT EXISTS "Notas" (
		"ID"	INTEGER NOT NULL UNIQUE,
		"Students"	TEXT NOT NULL,
		"P1"	INTEGER NOT NULL,
		"P2"	INTEGER NOT NULL,
		"P3"	INTEGER NOT NULL,
		"P4"	INTEGER NOT NULL,
		PRIMARY KEY("ID" AUTOINCREMENT)
	)""")

	con.commit()
	con.close()

def menu():
	init_db()
	
	while True:
		print("\n-----Notas De Los Estudiantes-----")
		print("1. Ingresar Estudiante")
		print("2. Ver Notas Guardadas")
		print("3. Salir")

		option = input("Elige una opción: ")
		
		match option:
			case '1':
				add_Stu()
			case '2':
				print("Opcion no implementada :(")
				show_Grades()
			case '3':
				break
			case _:
				print("\nError: Opcion no valida")
if __name__ == "__main__":
	menu()
