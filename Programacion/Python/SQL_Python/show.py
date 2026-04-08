import sqlite3
def promParcial(P1,P2):
	grades = [P1,P2]
	result = sum(grades) / len(grades)
	return result	
 
def promTotal(P1,P2,P3,P4):
    grades = [P1,P2,P3,P4]
    result = sum(grades) / len(grades)
    return result
    

def show_Grades():
	con = sqlite3.connect("Sql.db")
	cur = con.cursor()
	
	print("\n--- Notas Escolares ---")

	cur.execute("SELECT Students, P1, P2, P3, P4 FROM Notas")
	
	regs = cur.fetchall()
	
	if not regs:
		print("No hay registro")
	else:
		for reg in regs:
			print(f"Estudiante: {reg[0]} \n Notas P1: {reg[1]} | P2: {reg[2]} | P3: {reg[3]} | P4: {reg[4]} | Parcial: {promParcial(reg[1],reg[2])} Total: {promTotal(reg[1],reg[2],reg[3],reg[4])}")
	con.close()

if __name__ == "__main__":
	show_Grades()
