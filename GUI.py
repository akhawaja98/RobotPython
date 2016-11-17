from tkinter import *

class gui:
    def __init__(self, master):
        self.master = master
        master.title("Virtual simulator")

        self.label = Label(master, text="Welcome to our virtual simulator")
        self.label.pack()

        self.greet_button = Button(master, text="Start", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Let's start")


    def quit(self):
        exit()
        
root = Tk()
my_gui = gui(root)
root.mainloop()

