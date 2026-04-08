import sqlite3

def add_Stu():
	con = sqlite3.connect("Sql.db")
	cur = con.cursor()
	
	into = ("INSERT INTO Notas (Students, P1, P2, P3, P4) VALUES (?, ?, ?, ?, ?)")
	
	stu = input("Nombre del estudiante: ")
	P1 = input("Nota del P1: ")
	P2 = input("Nota del P2: ")
	P3 = input("Nota del P3: ")
	P4 = input("Nota del P4: ")
 
	cur.execute(into, (stu, P1, P2, P3, P4))
	
	con.commit()
	con.close()
	
	print("Notas guardas correntamente!")

if __name__ == "__main__":
	add_Stu()
