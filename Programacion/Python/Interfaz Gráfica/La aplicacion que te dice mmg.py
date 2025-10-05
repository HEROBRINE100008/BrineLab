import tkinter as tk

def Enviar():
    aw = bar.get().strip().lower()
    if aw == "si":
        aw2 = tk.Label(text="MMG")
        aw2.pack()
    elif aw == "no":
        aw3 = tk.Label(text="MMG como quiera ooo, mi boca e' mia coño")
        aw3.pack()
    else:
        aw4 = tk.Label(text="No se que tu dijite pero MMG")
        aw4.pack()
    

window = tk.Tk()
window.title("La app que de dice mmg")
window.geometry("700x400")

qt = tk.Label(text="Quieres que te diga MMG?(Si/No)")
qt.pack()

bar = tk.Entry(window)
bar.pack()


bt = tk.Button(text="Enviar", command=Enviar)
bt.pack()

window.mainloop()