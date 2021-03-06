from tkinter import *

def MainBackground():
    w.create_rectangle(0, 0, 1280, 720, fill="dark green")

def Road1(x, y):
    w.create_rectangle(x, y, 680, 720, fill="#55290D")
def Road2(x, y):
    w.create_line(x, y, 600, 1000, width=40, fill="#55290D")
def Road3(x, y):
    w.create_line(x, y, 380, 720, width=40, fill="#55290D")
def Road4(x, y):
    w.create_line(x, y, 800, 720, width=40, fill="#55290D")
def Road5(x, y):
    w.create_line(x, y, 940, 720, width=40, fill="#55290D")

def Landmark(x, y):
    w.create_rectangle(x, y, 740, 360, fill="#FF00D4")
def Landmark2(x, y):
    w.create_rectangle(x, y, 610, 40, fill="#FF00D4")
def Landmark3(x, y):
    w.create_rectangle(x, y, 460, 160, fill="#FF00D4")
def Landmark4(x, y):
    w.create_rectangle(x, y, 380, 540, fill="#FF00D4")
def Landmark5(x, y):
    w.create_rectangle(x, y, 1000, 400, fill="#FF00D4")
def Landmark6(x, y):
    w.create_rectangle(x, y, 1200, 300, fill="#FF00D4")



root = Tk()
root.geometry("1280x720")

w = Canvas(root, width=1280, height=720)
w.pack()

MainBackground()
Road1(630, 0)
Road2(20, -1200)
Road3(10, -10)
Road4(950, -10)
Road5(1270, -10)
Landmark(700, 400)
Landmark2(570, 80)
Landmark3(420, 200)
Landmark4(340, 580)
Landmark5(960, 440)
Landmark6(1160, 340)

root.mainloop()
