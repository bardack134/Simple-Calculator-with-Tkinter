from tkinter import *
root = Tk( )
b=0
for r in range(3):
    for c in range(3):
        b=b+1
        Button(root, text=str(b),
        borderwidth=1 ).grid(row=r,column=c)
root.mainloop()