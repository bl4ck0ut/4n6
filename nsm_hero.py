import Tkinter
import tkMessageBox
from Tkinter import *
from ttk import Frame, Button, Style
import os

top = Tkinter.Tk()

def readline():
   f=file("/etc/group")
   while True:
      line = f.readline()
      if len(line) == 0:
         break
      print line.strip()
   f.close()

def sguil():
   import subprocess
   subprocess.Popen(["sudo","python","./hero1/hero1.py"])

def tcpreplay():
   if button["text"] == "Start Hero #1":
      button["text"] = "Hero #1 running"
      button["bg"] = "green"
      button["activebackground"] = "green"
      import subprocess
      subprocess.Popen(["tcpreplay", "--intf1=eth0", "/home/cpfaff/Desktop/98.pcap"])
      return
   else:
      button["text"] = "Start Hero #1"
      button["bg"] = "red"
      button["activebackground"] = "red"
      import subprocess
      subprocess.Popen(["killall", "tcpreplay"])


def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Welcome to NSM Hero!!")

img = PhotoImage(file="/home/cpfaff/Downloads/download.gif")
panel = Label(top, image=img)

panel.grid(row=0, column=0, columnspan=2, rowspan=7, sticky=W+E+N+S, padx=5, pady=5)


D = Tkinter.Button(top, text ="NSM HERO #1", command = sguil)
D.grid(row=2, column=0, sticky=W+E, columnspan=4)
D = Tkinter.Button(top, text ="NSM HERO #2", command = sguil)
D.grid(row=3, column=0, sticky=W+E, columnspan=4)
top.mainloop()
