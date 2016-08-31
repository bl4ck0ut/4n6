import Tkinter
import tkMessageBox
import subprocess
from Tkinter import *
from ttk import Frame, Button, Style

top = Tkinter.Tk()

def arena1():
   subprocess.Popen(["cp", "./arena1/rule/arena1.rule", "/etc/nsm/rules/local.rules"])
   subprocess.Popen(["sudo","python","./arena1/arena1.py"])

def arena2():
   subprocess.Popen(["sudo","python","./arena2/arena2.py"])

def arena3():
   subprocess.Popen(["sudo","python","./arena2/arena3.py"])

def arena4():
   subprocess.Popen(["sudo","python","./arena2/arena4.py"])

def arena5():
   subprocess.Popen(["sudo","python","./arena2/arena5.py"])

def tcpreplay():
   if button["text"] == "Start Arena #1":
      button["text"] = "Arena #1 running"
      button["bg"] = "green"
      button["activebackground"] = "green"
      subprocess.Popen(["tcpreplay", "--intf1=eth0", "/home/xxxx/Desktop/98.pcap"])
      return
   else:
      button["text"] = "Start Arena #1"
      button["bg"] = "red"
      button["activebackground"] = "red"
      subprocess.Popen(["killall", "tcpreplay"])

img = PhotoImage(file="./images/background.gif")
panel = Label(top, image=img)
panel.grid(row=0, column=0, columnspan=2, rowspan=7, sticky=W+E+N+S, padx=6, pady=6)
A = Tkinter.Button(top, text ="NSM HERO #1", command = arena1)
A.grid(row=1, column=0, sticky=W+E, columnspan=4)
B = Tkinter.Button(top, text ="NSM HERO #2", command = arena2)
B.grid(row=2, column=0, sticky=W+E, columnspan=4)
C = Tkinter.Button(top, text ="NSM HERO #3", command = arena3)
C.grid(row=3, column=0, sticky=W+E, columnspan=4)
D = Tkinter.Button(top, text ="NSM HERO #4", command = arena4)
D.grid(row=4, column=0, sticky=W+E, columnspan=4)
arena5 = Tkinter.Button(top, text ="NSM HERO #5", command = arena5)
arena5.grid(row=5, column=0, sticky=W+E, columnspan=4)

top.mainloop()
