from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
class myApp(object):
    def __init__(self, parent):
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        drawpad.pack()
        root.bind_all('<Key>', self.key)
    def key(self,event):
        if event.char == "a":
            print "a"
        
app = myApp(root)
root.mainloop()