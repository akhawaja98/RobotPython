import os             #Modules Imported.
import subprocess
import webbrowser
from tkinter import *

def MainBackground(): #This makes the background turn darkgreen.
    w.create_rectangle(0, 0, 1280, 720, fill="dark green")

root = Tk()
root.geometry("1280x720") #Creates a window that is in 720p
root.title('Menu!')

def closewindow(): #This module closes the window.
    exit()
CloseBtn= Button(root, text="Close The Program", command=closewindow, fg='dark green') #This creates a button, that executes the closing program function.
CloseBtn.pack(fill=BOTH, expand=1)


def openInstructions(): #Using the module webbrowser to open a text file.
    #Instructions= open('Instructions.txt')
    #info = Instructions.readlines()
    #print (info)                       Alternative way to open this.
    #Instructions.close()
    webbrowser.open("Instructions.txt") #opens file.
    
InstructionsBtn = Button(root, text='Instructions', command=openInstructions,fg='dark green')
InstructionsBtn.pack(fill=BOTH, expand=1)

def ShowText(): # This function desplays the text.
    text = Label(root, text = 'Welcome to the US Tour Guide!', font='Times 24 bold italic', fg='dark green')
    text.pack()
    text.place(x=440, y=360) # This places the text in the middle of the screen.

def openGame(): #This opens the actual game.
    os.system('foundation4.py')
GameBtn = Button(root, text='Start The Game!', command=openGame,fg='dark green')
GameBtn.pack(fill=BOTH, expand=1)



w = Canvas(root, width=1280, height=720)
w.pack()

ShowText()
MainBackground()
root.mainloop()

