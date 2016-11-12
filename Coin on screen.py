from tkinter import *

root = Tk() 

coin = PhotoImage(file="/media/removable/SD Card/Python - PUT INTO MEM STICK/TK/Coin.gif", 
                  format = "gif -index 0"  ) # Opening image of coin
w1 = Label(root, image=coin).pack(side = "right")


        

Text = Label(root,
            text="Coin Counter = 0",
            font = ('Times')).pack(side = "left") # Showing the counter



root.mainloop()
