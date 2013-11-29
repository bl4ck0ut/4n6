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
   subprocess.Popen(["sguil.tk"])

def lr_term1():
   import subprocess
   subprocess.Popen(["xfce4-terminal", "--working-directory=./hero1/56.101/"])

def lr_term2():
   import subprocess
   subprocess.Popen(["xfce4-terminal", "--working-directory=./hero1/56.102/"])

def tcpreplay():
   if button["text"] == "Start Hero #1":
      button["text"] = "Hero #1 running"
      button["bg"] = "green"
      button["activebackground"] = "green"
      import subprocess
      subprocess.Popen(["/usr/bin/pulledpork.pl", "-n", "-c" ,"/etc/nsm/pulledpork/pulledpork.conf"])
      subprocess.Popen(["/usr/sbin/nsm_sensor_ps-restart" ,"--only-snort-alert"])
      subprocess.Popen(["tcpreplay", "--intf1=eth0", "./hero1/network.pcap"])
      return
   else:
      button["text"] = "Start Hero #1"
      button["bg"] = "red"
      button["activebackground"] = "red"
      import subprocess
      subprocess.Popen(["killall", "tcpreplay"])


def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Welcome to NSM Hero!!")

B = Tkinter.Button(top, text ="Intro", command = helloCallBack)
C = Tkinter.Button(top, text ="check / Change Hero Rule", command = readline)
D = Tkinter.Button(top, text ="start sguil", command = sguil)
button = Tkinter.Button(top, activebackground = "red", text ="Start Hero #1", command = tcpreplay, bg = "red")
system1 = Tkinter.Button(top, text ="192.168.56.101 Live Response", command = lr_term1)
system2 = Tkinter.Button(top, text ="192.168.56.102 Live Response", command = lr_term2)
img = PhotoImage(file="./images/background.gif")
panel = Label(top, image=img)

panel.grid(row=0, column=1, columnspan=2, rowspan=7, sticky=W+E+N+S, padx=5, pady=5)
B.grid(row=0, column=0, sticky=W+E)
C.grid(row=1, column=0, sticky=W+E)
D.grid(row=2, column=0, sticky=W+E)
button.grid(row=3, column=0)
system1.grid(row=4, column=0)
system2.grid(row=5, column=0)

top.mainloop()
