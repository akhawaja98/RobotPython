from tkinter import *

root = Tk()
global startlives
startlives = 3

startliveslabel = Label(root, text= "You Have 3 Lives, Good Luck", font="Times")
startliveslabel.pack()


def printlives():    
    global startlives
    startlives -= 1
    startliveslabel.config(text="You Have " + str(startlives) + " Lives")

    if startlives <= 0:
        startliveslabel.config(text="GAME OVER - No Lives Left")


    if startlives == 1:
        startliveslabel.config(text="You Have 1 Life Left")
        


loselifebtn = Button(root, text="Lost Life", command=printlives)
loselifebtn.pack()

root.mainloop()
