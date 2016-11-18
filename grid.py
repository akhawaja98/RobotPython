from tkinter import *

def checkered(canvas, line_distance):
   for a in range(line_distance,canvas_width,line_distance): #this makes vertical lines for grid
      canvas.create_line(a, 0, a, canvas_height, fill="#476042")
   for b in range(line_distance,canvas_height,line_distance): #this makes vertical lines for grid
      canvas.create_line(0, b, canvas_width, b, fill="#476042")

master = Tk()
canvas_width = 1280
canvas_height = 720 
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

checkered(w,10)

mainloop()
