import tkinter as tk

window = tk.Tk()

button = tk.Button(
    text = "Click me!",
    width=25,
    height=5,
    bg="#0000ff",
    fg="#ffff00",
    )
button.pack()

window.mainloop()