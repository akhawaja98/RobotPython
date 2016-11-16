from tkinter import *


root = Tk()

startinglives = Label(root, text= "You Have 3 Lives, Good Luck")
startinglives.pack()

button1 = Button(root, text="Lost Life")
button1.pack()


root.mainloop()
