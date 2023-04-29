import tkinter as tk
from tkinter.font import BOLD
import utileri.generic as utl

class MasterPanel:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Master Panel")
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.config(bg="#fcfcfc")
        self.root.resizable(height=0, width=0)
    

        logo = utl.leer_imagen("./imagenes/cato.png", (300,300))

        label = tk.Label(self.root, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relheight= 1, relwidth=1)
        self.root.mainloop()