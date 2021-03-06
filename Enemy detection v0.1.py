import math
import time
#import winsound
from tkinter import *

def MainBackground():

    w.create_rectangle(0, 0, 1280, 720, fill="dark green")

def Road1(x, y):

    w.create_rectangle(x, y, 680, 720, fill="#55290D")

def Road2(x, y):

    w.create_line(x, y, 600, 1000, width=40, fill="#55290D")

def Road3(x, y):

    w.create_line(x, y, 380, 720, width=40, fill="#55290D")

def Road4(x, y):

    w.create_line(x, y, 800, 720, width=40, fill="#55290D")

def Road5(x, y):

    w.create_line(x, y, 940, 720, width=40, fill="#55290D")

def Landmark(x, y):

    w.create_rectangle(x, y, 740, 360, fill="#FF00D4")

def Landmark2(x, y):

    w.create_rectangle(x, y, 610, 40, fill="#FF00D4")

def Landmark3(x, y):

    w.create_rectangle(x, y, 460, 160, fill="#FF00D4")

def Landmark4(x, y):

    w.create_rectangle(x, y, 380, 540, fill="#FF00D4")

def Landmark5(x, y):

    w.create_rectangle(x, y, 1000, 400, fill="#FF00D4")

def Landmark6(x, y):

    w.create_rectangle(x, y, 1200, 300, fill="#FF00D4")

def Platform(x, y):

    w.create_rectangle(x, y, 1400, 680, width =0, fill="#55290D")

root = Tk()

root.geometry("1280x720")

w = Canvas(root, width=1280, height=720)

w.pack()

MainBackground()

Road1(630, 0)

Road2(20, -1200)

Road3(10, -10)

Road4(950, -10)

Road5(1270, -10)

Landmark(700, 400)

Landmark2(570, 80)

Landmark3(420, 200)

Landmark4(340, 580)

Landmark5(960, 440)

Landmark6(1160, 340)

Platform(0, 800)

Robot= w.create_oval(1230,690,1250,710, fill="#000000")

def leftKey(event):

    x1,y1,x2,y2 = w.coords(Robot)

    w.coords(Robot,x1-10,y1,x2-10,y2)

def rightKey(event):

    x1,y1,x2,y2= w.coords(Robot)

    w.coords(Robot,x1+10,y1,x2+10,y2)

def upKey(event):

     x1,y1,x2,y2= w.coords(Robot)

     w.coords(Robot,x1,y1-5,x2,y2-5)

def downKey(event):

     x1,y1,x2,y2= w.coords(Robot)

     w.coords(Robot,x1,y1+5,x2,y2+5)

w.bind('<Left>', leftKey)

w.bind('<Right>', rightKey)

w.bind('<Up>', upKey)

w.bind('<Down>', downKey)

w.focus_set()

x_min = 3

y_min = 3

x_max = 1260

y_max = 715

def distance():

    start = w.create_rectangle(1260, 675, 1279, 719, fill="green")

    finish = w.create_rectangle(0, 675, 19, 719, fill="red")

    f1, f2, f3, f4 = w.coords(finish)

    s1, s2, s3, s4 = w.coords(start)

    distanceFrom = math.sqrt((s1 - f1)**2 + (s2 - f2)**2)

    print(str(distanceFrom))

def neverEndingFunctions():

    def collisionDetection():

        cx = 0

        cy = 0

        ball = w.create_oval(10,10,60,60, fill="#FF0000")

        XSpeed = 1

        YSpeed = 2

    

        while True:

            w.move(ball, XSpeed, YSpeed)

            Pos = w.coords(ball)

            if Pos[3] >=720 or Pos[1] <=0:

                YSpeed = -YSpeed

            if Pos[2] >=1280 or Pos[0] <=0:

                XSpeed = -XSpeed

                

            rx1, ry1, rx2, ry2 = w.coords(Robot)

            if rx1 >= x_max:

                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)

                cx = -10

            if ry1 <= y_min:

                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)

                cy = 10

            if ry2 >= y_max:

                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)

                cy= -10

            if rx1 <= x_min:

                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)

                cx = 10

            w.coords(Robot, rx1+cx, ry1+cy, rx2+cx, ry2+cy)

            cx = 0

            cy = 0

            ex1, ey1, ex2, ey2 = w.coords(Enemy)
 
            if rx1 == ex1 or rx1 == ey1 or rx1 == ex2 or rx1 == ey2:
                print("Robot hit enemy")
            if rx2 == ex1 or rx2 == ey1 or rx2 == ex2 or rx2 == ey2:
                print("Robot hit enemy")
            if ry1 == ex1 or ry1 == ey1 or ry1 == ex2 or ry1 == ey2:
                print("Robot hit enemy")
            if ry2 == ex1 or ry2 == ey1 or ry2 == ex2 or ry2 == ey2:
                print("Robot hit enemy")
        

            w.update()

            time.sleep(0.01)

            

    collisionDetection()

distance()
