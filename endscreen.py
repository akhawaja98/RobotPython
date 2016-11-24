from tkinter import *

def QuitGame(event=None):
    regionFrame.destroy()


regionFrame = Tk()
regionFrame.geometry("1280x720")
regionFrame.title("End Screen")

def background():
    EndScreen = Canvas(regionFrame, width = 1280, height = 720, bg = "dark red")
    #EndScreen.create_rectangle(0, 0, 1280, 720, fill="dark red")
    EndScreen.pack()

EndText = Label(regionFrame, text="Game Over", font="times")
EndText.pack(side="top")

QuitButton = Button(regionFrame, text="Quit", font="times",
                    width=1280, height=2, command=QuitGame).pack(side="top")

#coincounter text
LandmarkCounter = Label(regionFrame, text="Landmarks visited = ", font="times")
LandmarkCounter.pack(side="top")

background()
regionFrame.mainloop()
