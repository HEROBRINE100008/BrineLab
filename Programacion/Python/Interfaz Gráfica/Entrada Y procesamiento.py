import tkinter as tk

def enviar():
    name = entry.get()
    label2 = tk.Label(text=name)
    label2.pack()

    
window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry(window)
label.pack()
entry.pack()


button = tk.Button(text="Enviar", command=enviar)
button.pack()


window.mainloop()