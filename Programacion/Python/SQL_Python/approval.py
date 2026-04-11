import sqlite3
from show import promTotal

def appr():
    con = sqlite3.connect("Sql.db")
    cur = con.cursor()
    
    cur.execute("SELECT Students, P1, P2, P3, P4 FROM Notas")
    regs = cur.fetchall()

    if not regs:
        print("No hay nada en el registro")
        
    else: 
        for reg in regs:
            approval = prom(reg[1], reg[2], reg[3], reg[4]) 
            if approval >= 70:
                print(f"{reg[0]}               \t| Resultado: Aprobado")
            else:
                print(f"{reg[0]}               \t| Resultado: Reprobado")
            
    con.close()
    
prom = promTotal

if __name__ == "__main__":
    appr()