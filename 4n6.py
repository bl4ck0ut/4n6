import Tkinter
import tkMessageBox
import subprocess
from Tkinter import *
from ttk import Frame, Button, Style

master = Tk()
master.resizable(width=True, height=True)
master.geometry('200x200')
img = PhotoImage(file="./images/background.gif")
background_label = Tkinter.Label(master, image=img)
background_label.place(x=0, y=55, relwidth=1, relheight=1)


var = StringVar(master)
var.set("arena1") # initial value

option = OptionMenu(master, var, "arena1", "arena2", "arena3", "arena4","arena5")
option.config(bg = "GREEN")
option.pack()

def arena():
   subprocess.Popen(["cp", "./"+var.get()+"/rule/"+ var.get()+".rule", "/etc/nsm/rules/local.rules"])
   subprocess.Popen(["sudo","python","./"+var.get()+"/"+var.get()+".py"])

button = Button(master, text="Run!!", command=arena)
button.pack()


mainloop()
