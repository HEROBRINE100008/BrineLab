import sqlite3

def add_Stu():
	con = sqlite3.connect("Sql.db")
	cur = con.cursor()
	
	into = ("INSERT INTO Notas (Students, Grades) VALUES (?, ?)")
	
	stu = input("Nombre del estudiante: ")
	sco = input("Nota: ")
	
	cur.execute(into, (stu, sco))
	
	con.commit()
	con.close()
	
	print("Notas guardas correntamente!")

if __name__ == "__main__":
	add_Stu()
