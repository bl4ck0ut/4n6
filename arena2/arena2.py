import Tkinter
import tkMessageBox
import subprocess
from Tkinter import *
from ttk import Frame, Button, Style
import os

top = Tkinter.Tk()

def gedit_localrules():
   subprocess.Popen(["gedit", "/etc/nsm/rules/local.rules"])

def sguil():
   subprocess.Popen(["sguil.tk"])

def lr_term1():
   subprocess.Popen(["xfce4-terminal", "--working-directory=./arena2/56.101/"])

def tcpreplay():
   if button["text"] == "Start Arena #2":
      button["text"] = "Arena #2 running"
      button["bg"] = "green"
      button["activebackground"] = "green"
      subprocess.Popen(["sguil.tk"])
      subprocess.Popen(["/usr/bin/pulledpork.pl", "-n", "-c" ,"/etc/nsm/pulledpork/pulledpork.conf"])
      subprocess.Popen(["/usr/sbin/nsm_sensor_ps-restart"])
      subprocess.Popen(["tcpreplay", "--intf1=eth0", "./arena2/network.pcap"])
      return
   else:
      button["text"] = "Start Arena #2"
      button["bg"] = "red"
      button["activebackground"] = "red"
      subprocess.Popen(["killall", "tcpreplay"])

def arena1intro():
   tkMessageBox.showinfo( "Arena #2", "Welcome to NSM Arena!! \n This is an extercise that was already done but I added the LR and this also puts you in the hotseat. If you want to get the answers follow this link. http://www.malware-traffic-analysis.net/2013/09/07/index.html")

B = Tkinter.Button(top, text ="Intro", command = arena1intro)
C = Tkinter.Button(top, text ="check / Change Arena Rule", command = gedit_localrules)
D = Tkinter.Button(top, text ="start sguil", command = sguil)
button = Tkinter.Button(top, activebackground = "red", text ="Start Arena #2", command = tcpreplay, bg = "red")
system1 = Tkinter.Button(top, text ="192.168.56.101 Live Response", command = lr_term1)
img = PhotoImage(file="./images/background.gif")
panel = Label(top, image=img)

panel.grid(row=0, column=1, columnspan=2, rowspan=7, sticky=W+E+N+S, padx=5, pady=5)
B.grid(row=0, column=0, sticky=W+E)
C.grid(row=1, column=0, sticky=W+E)
D.grid(row=2, column=0, sticky=W+E)
button.grid(row=3, column=0)
system1.grid(row=4, column=0)

top.mainloop()
