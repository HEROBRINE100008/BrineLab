import sqlite3

def show_Grades():
	con = sqlite3.connect("Sql.db")
	cur = con.cursor()
	
	print("\n--- Notas Escolares ---")

	cur.execute("SELECT Students, Grades FROM Notas")
	
	regs = cur.fetchall()
	
	if not regs:
		print("No hay registro")
	else:
		for reg in regs:
			print(f"Estudiante: {reg[0]} | Nota: {reg[1]}")
	con.close()

if __name__ == "__main__":
	show_Grades()
