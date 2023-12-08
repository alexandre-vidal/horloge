from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Horloge")

def afficher_heure():
    string = strftime('%D | %H:%M:%S')
    label.config(text=string)
    label.after(1000, afficher_heure)

label = Label(root, font=("Arial", 80), background = "black", foreground = "white")
label.pack(anchor='center')
afficher_heure()

mainloop()