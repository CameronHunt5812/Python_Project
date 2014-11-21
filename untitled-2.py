from Tkinter import *
import math
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
drawpad.create_oval(100,300,200,400)
a = 150
b = 350
angle = 90
r = math.cos(angle)

drawpad.create_line(a+r*math.cos(angle), b+r*math.sin(angle),0,0,arow = "true")


root.mainloop()