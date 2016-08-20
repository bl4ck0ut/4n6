import Tkinter
import tkMessageBox
import subprocess
from Tkinter import *
from ttk import Frame, Button, Style

top = Tkinter.Tk()

def hero1():
   subprocess.Popen(["cp", "./hero1/rule/hero1.rule", "/etc/nsm/rules/local.rules"])
   subprocess.Popen(["sudo","python","./hero1/hero1.py"])

def hero2():
   subprocess.Popen(["sudo","python","./hero2/hero2.py"])

def hero3():
   subprocess.Popen(["sudo","python","./hero2/hero3.py"])

def hero4():
   subprocess.Popen(["sudo","python","./hero2/hero4.py"])

def hero5():
   subprocess.Popen(["sudo","python","./hero2/hero5.py"])

def tcpreplay():
   if button["text"] == "Start Hero #1":
      button["text"] = "Hero #1 running"
      button["bg"] = "green"
      button["activebackground"] = "green"
      subprocess.Popen(["tcpreplay", "--intf1=eth0", "/home/cpfaff/Desktop/98.pcap"])
      return
   else:
      button["text"] = "Start Hero #1"
      button["bg"] = "red"
      button["activebackground"] = "red"
      subprocess.Popen(["killall", "tcpreplay"])

img = PhotoImage(file="./images/background.gif")
panel = Label(top, image=img)
panel.grid(row=0, column=0, columnspan=2, rowspan=7, sticky=W+E+N+S, padx=6, pady=6)
A = Tkinter.Button(top, text ="NSM HERO #1", command = hero1)
A.grid(row=1, column=0, sticky=W+E, columnspan=4)
B = Tkinter.Button(top, text ="NSM HERO #2", command = hero2)
B.grid(row=2, column=0, sticky=W+E, columnspan=4)
C = Tkinter.Button(top, text ="NSM HERO #3", command = hero3)
C.grid(row=3, column=0, sticky=W+E, columnspan=4)
D = Tkinter.Button(top, text ="NSM HERO #4", command = hero4)
D.grid(row=4, column=0, sticky=W+E, columnspan=4)
hero5 = Tkinter.Button(top, text ="NSM HERO #5", command = hero5)
hero5.grid(row=5, column=0, sticky=W+E, columnspan=4)

top.mainloop()
