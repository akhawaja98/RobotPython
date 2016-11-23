import os
import subprocess
from tkinter import *

def MainBackground():
    w.create_rectangle(0, 0, 1280, 720, fill="dark green")

root = Tk()
root.geometry("1280x720")
root.title('Menu!')

def closewindow():
    exit()
CloseBtn= Button(root, text="Close The Program", command=closewindow, fg='dark green')
CloseBtn.pack(fill=BOTH, expand=1)


def openInstructions():
    Instructions= open('Instructions.txt')
    info = Instructions.readlines()
    print (info)
    Instructions.close()
InstructionsBtn = Button(root, text='Instructions', command=openInstructions,fg='dark green')
InstructionsBtn.pack(fill=BOTH, expand=1)

def ShowText():
    text = Label(root, text = 'Welcome to the US Tour Guide!', font='Times 24 bold italic', fg='dark green')
    text.pack()
    text.place(x=440, y=360)

def openGame():
    Command= "Foundation3 - Shortcut"
    subprocess.Popen(Command)
GameBtn = Button(root, text='Start The Game!', command=openGame,fg='dark green')
GameBtn.pack(fill=BOTH, expand=1)



w = Canvas(root, width=1280, height=720)
w.pack()

ShowText()
MainBackground()
root.mainloop()

