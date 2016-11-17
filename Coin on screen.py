from tkinter import *

def Collected(event=None):
    global CoinCounter
    CoinCounter += 1
    Text.config(text="Coin Counter = " + str(CoinCounter))

    
root = Tk()
root.geometry("500x500")
root.title("Coin module")

global CoinCounter
CoinCounter = 0

coin = PhotoImage(file="/media/removable/SD Card/Python - PUT INTO MEM STICK/TK/Coin.gif", 
                  format = "gif -index 0" ) # Opening image of coin

w1 = Label(root, image=coin).pack(side = "left")

Text = Label(root,
            text="Coin Counter = 0" ,
            font = ('Times'))# Showing the counter
Text.pack(side = "right")

CollectCoin = Button(root, text="Collect", command=Collected).pack(side = "left")


        







root.mainloop()
