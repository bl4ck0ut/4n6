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
panel.grid(row=0, column=0, columnspan=2, rowspan=7, sticky=W+E+N+S, padx=5, pady=5)
A = Tkinter.Button(top, text ="NSM HERO #1", command = hero1)
A.grid(row=2, column=0, sticky=W+E, columnspan=4)
B = Tkinter.Button(top, text ="NSM HERO #2", command = hero2)
B.grid(row=3, column=0, sticky=W+E, columnspan=4)
top.mainloop()
