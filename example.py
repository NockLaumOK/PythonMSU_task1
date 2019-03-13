#!/usr/bin/env python3

from tkinter import *
def fnB(*args):
	print("QQ", *args)

root = Tk()

Butt = Button(root, command=fnB,  text="Butt ON")
Butt.grid()

root.mainloop()
print("QQ") #prints after closing
root.destroy()