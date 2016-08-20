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
   subprocess.Popen(["xfce4-terminal", "--working-directory=./hero2/56.101/"])

def lr_term2():
   subprocess.Popen(["xfce4-terminal", "--working-directory=./hero2/56.102/"])

def tcpreplay():
   if button["text"] == "Start Hero #2":
      button["text"] = "Hero #2 running"
      button["bg"] = "green"
      button["activebackground"] = "green"
      subprocess.Popen(["/usr/bin/pulledpork.pl", "-n", "-c" ,"/etc/nsm/pulledpork/pulledpork.conf"])
      subprocess.Popen(["/usr/sbin/nsm_sensor_ps-restart"])
      subprocess.Popen(["tcpreplay", "--intf1=eth0", "./hero2/network.pcap"])
      return
   else:
      button["text"] = "Start Hero #2"
      button["bg"] = "red"
      button["activebackground"] = "red"
      subprocess.Popen(["killall", "tcpreplay"])

def hero1intro():
   tkMessageBox.showinfo( "Hero #1", "Welcome to NSM Hero!! \n This is the first Hero. This is the first hero since it was my first I had to deal with back in early 2000. The object will be to start sguil then start hero #1 and wait. \n \n You are now in the hot seat to determine what is going on. I have created a skeleton snort rule that will fire , again this is generic. The idea is to figure out what it is and rewrite the rule and rerun the hero and see how you do. There is a live response section that will help you along the way as well.")

B = Tkinter.Button(top, text ="Intro", command = hero1intro)
C = Tkinter.Button(top, text ="check / Change Hero Rule", command = gedit_localrules)
D = Tkinter.Button(top, text ="start sguil", command = sguil)
button = Tkinter.Button(top, activebackground = "red", text ="Start Hero #2", command = tcpreplay, bg = "red")
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
