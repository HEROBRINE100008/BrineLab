import tkinter as tk

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

window = tk.Tk()

label = tk.Label(
    text = "hello, tinker",
    foreground=_from_rgb((255, 0, 0)),
    background = "black",
    width = 10,
    height=10
)
label.pack()

window.mainloop()