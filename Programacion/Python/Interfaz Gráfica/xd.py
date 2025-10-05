import tkinter as tk
import pygubu

class App:
    def __init__(self):
        self.builder = pygubu.Builder()
        self.builder.add_from_file('diseño.ui')
        self.root = self.builder.get_object('mainwindow')
        self.builder.connect_callbacks(self)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()