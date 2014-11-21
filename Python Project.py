from Tkinter import *
import math
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
drawpad.create_oval(250,100,550,300)
angle = 0

class myApp(object):
    def __init__(self, parent):
        drawpad.pack()
        root.bind_all('<Key>',self.key)
    def key(self,event):
        global angle
        cosb = math.cos(angle + 8.3)
        sinb = math.sin(angle + 8.3)
        if event.char == "a":
            angle = angle - 0.03
        elif event.char == "d":
            angle = angle + 0.03
        ax1 = 350 + 150 * math.cos(angle)
        ay1 = 200 + 100 * math.sin(angle)
        ax2 = 350 + 150 * math.cos(angle)
        ay2 = 400 + 100 * math.sin(angle)
        bx1 = 350 + 150 * cosb
        by1 = 200 + 100 * sinb
        bx2 = 350 + 150 * cosb
        by2 = 400 + 100 * sinb
        drawpad.delete(all)
        drawpad.create_line(ax2,ay2,ax1,ay1)
        drawpad.create_line(bx2,by2,bx1,by1)

app = myApp(root)
root.mainloop()