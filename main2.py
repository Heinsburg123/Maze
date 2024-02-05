from tkinter import *

root = Tk()
c=Canvas(root,bg='white',height=700,width=1500)
def click(event):
    x=event.x 
    y=event.y  
    print(x,y)
c.bind('<Button 1>',click)
c.pack
root.mainloop()