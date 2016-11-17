from tkinter import *
root = Tk()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
wall = PhotoImage(file = "D:\wall.png")
image = canvas.create_image(280, 30, anchor=NE, image=wall)
root.mainloop()
