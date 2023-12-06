from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Horloge")

def time():
    string = strftime('%D | %H:%M:%S')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Arial", 80), background = "black", foreground = "white")
label.pack(anchor='center')
time()

mainloop()