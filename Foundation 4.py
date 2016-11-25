import math
import time
import winsound
from tkinter import *
import random

def Collected(event=None):
    global CoinCounter
    CoinCounter += 1
    

def QuitScreen():
    QuitScreen = Tk()

    EndText = Label(QuitScreen, text="Game Over", font="times")
    EndText.pack(side="top")

   


    CoinText = Label(QuitScreen, text="Coins Collected = " + str(CoinCounter), font="times")
    CoinText.pack(side="top")
          
    	  

def MainBackground():
    w.create_rectangle(0, 0, 1280, 720, fill="dark green")

def Road1(x, y):
    w.create_rectangle(x, y, 680, 720, fill="#55290D")
def Road2(x, y):
    w.create_line(x, y, 600, 1000, width=40, fill="#55290D")
def Road3(x, y):
    w.create_line(x, y, 380, 720, width=40, fill="#55290D")
def Road4(x, y):
    w.create_line(x, y, 800, 720, width=40, fill="#55290D")         #Creating the objects used for the map visuals
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
def Platform(x, y):
    w.create_rectangle(x, y, 1400, 680, width =0, fill="#55290D")





root = Tk()
root.geometry("1280x720")
global startlives
global CoinCounter
CoinCounter = 0
startlives = 10 #sets number of starting lives -1

def PrintLives():    
      global startlives 	
      startliveslabel = Label(root, text= "You Have 3 Lives, Good Luck", font="Times")
      startliveslabel.place(x=100, y=30) #positioning the lives label in a suitable area of the canvas
  		  
      		      
      startlives -= 1
      startliveslabel.config(text="Health = " + str(startlives) + "%") #.config allows us to change the labels text
  		  
      if startlives == 0:	  		
          root.destroy()
        
          QuitScreen()	  
  		  
      if startlives == 1:
          startliveslabel.config(text="1% Health Left Be Careful")


w = Canvas(root, width=1280, height=720)    #Create canvas to start adding objects and drawings
w.pack()
MainBackground()


#750 = top right = x1
#175 = top left = y1
#200 = bottom right = y2
#725 = bottom left = x2
powerUp = w.create_rectangle(750, 175, 725, 200, fill="SeaGreen1")


Road1(630, 0)
Road2(20, -1200)
Road3(10, -10)
Road4(950, -10)
Road5(1270, -10)        #Call the functions to see the objects
Landmark(700, 400)
Landmark2(570, 80)
Landmark3(420, 200)
Landmark4(340, 580)
Landmark5(960, 440)
Landmark6(1160, 340)
Platform(0, 800)

Robot= w.create_oval(1230,690,1250,710, fill="#000000") #Creating the object for the robot

def leftKey(event):
    '''Functions to allow robot to move on button press'''
    x1,y1,x2,y2 = w.coords(Robot)
    w.coords(Robot,x1-10,y1,x2-10,y2)


def rightKey(event):
    x1,y1,x2,y2= w.coords(Robot)
    w.coords(Robot,x1+10,y1,x2+10,y2)


def upKey(event):
     x1,y1,x2,y2= w.coords(Robot)
     w.coords(Robot,x1,y1-10,x2,y2-10)


def downKey(event):
     x1,y1,x2,y2= w.coords(Robot)
     w.coords(Robot,x1,y1+10,x2,y2+10)

w.bind('<Left>', leftKey)
w.bind('<Right>', rightKey)
w.bind('<Up>', upKey)
w.bind('<Down>', downKey)
w.focus_set()

x_min = 3
y_min = 3
x_max = 1260    #Creating the borders so the robot does not escape
y_max = 715


def distance():
    start = w.create_rectangle(1260, 675, 1279, 719, fill="green")
    finish = w.create_rectangle(0, 675, 19, 719, fill="red")
    f1, f2, f3, f4 = w.coords(finish)
    s1, s2, s3, s4 = w.coords(start)
    distanceFrom = math.sqrt((s1 - f1)**2 + (s2 - f2)**2)
    print(str(distanceFrom))

def neverEndingFunctions():
    '''Function for code that is in constant loop'''
    def collisionDetection():
        cx = 0
        cy = 0
        ball = w.create_oval(10,10,60,60, fill="#FF0000")
        XSpeed = 1
        YSpeed = 2
    
        while True:
            w.move(ball, XSpeed, YSpeed)
            Pos = w.coords(ball)
            if Pos[3] >=720 or Pos[1] <=0:  #this is to make the enemy to move and bounce off borders of the screen
                YSpeed = -YSpeed
            if Pos[2] >=1280 or Pos[0] <=0:
                XSpeed = -XSpeed

            coincounter = 0


            p = list(w.bbox(Robot)) #get's latest coordinates of robot's position
        

            #checks if robot is near landmark6
            if p[0] >= 1100 and p[0] <= 1230 and p[1] >= 250 and p[1] <= 400 and p[2] >= 1100 and p[2] <= 1300 and p[3] >= 200 and p[3] <= 400:
                PromptLandMark6()
                Collected()
                
            #checks if robot is near landmark5
            elif p[0] >= 900 and p[0] <= 1030 and p[1] >= 350 and p[1] <= 500 and p[2] >= 900 and p[2] <= 1100 and p[3] >= 300 and p[3] <= 500:
                PromptLandMark5()

            #checks if robot is near landmark4
            elif p[0] >= 260 and p[0] <= 410 and p[1] >= 490 and p[1] <= 640 and p[2] >= 280 and p[2] <= 480 and p[3] >= 440 and p[3] <= 640:
                PromptLandMark4()
                Collected()

            
            #checks if robot is near landmark3
            elif p[0] >= 340 and p[0] <= 490 and p[1] >= 110 and p[1] <= 260 and p[2] >= 360 and p[2] <= 560 and p[3] >= 60 and p[3] <= 260:
                PromptLandMark3()
                Collected()

            #checks if robot is near landmark2
            elif p[0] >= 490 and p[0] <= 640 and p[1] >= 0 and p[1] <= 140 and p[2] >= 510 and p[2] <= 710 and p[3] >= 0 and p[3] <= 140:
                PromptLandMark2()
                Collected()

            #checks if robot is near landmark1
            elif p[0] >= 620 and p[0] <= 770 and p[1] >=310  and p[1] <= 460 and p[2] >= 640 and p[2] <= 840 and p[3] >= 220 and p[3] <= 440:
                PromptLandMark1()
                Collected()

                
            PosR = w.bbox(Robot)
            #This code measures the distance between the robot and the enemy
            enemydist = int(math.sqrt((int(PosR[2]) - int(Pos[2]))**2 + (int(PosR[3]) - int(Pos[3]))**2))

            #This code measures the distance between the robot and Landmarks
            landmar1kdist = int(math.sqrt( (int(PosR[2]) - 370)**2 + (int(PosR[3]) - 580)**2))
            landmar2kdist = int(math.sqrt( (int(PosR[2]) - 450)**2 + (int(PosR[3]) - 195)**2))
            landmar3kdist = int(math.sqrt( (int(PosR[2]) - 610)**2 + (int(PosR[3]) - 80)**2))
            landmar4kdist = int(math.sqrt( (int(PosR[2]) - 740)**2 + (int(PosR[3]) - 400)**2))
            landmar5kdist = int(math.sqrt( (int(PosR[2]) - 1000)**2 + (int(PosR[3]) - 440)**2))
            landmar6kdist = int(math.sqrt( (int(PosR[2]) - 1200)**2 + (int(PosR[3]) - 340)**2))
            #This code finds nearest landmark
            LandmarkList = (landmar1kdist, landmar2kdist, landmar3kdist, landmar4kdist, landmar5kdist, landmar6kdist)
            NearestLandmark = min(LandmarkList)
            nearestLandm = Label(root, text = "Nearest landmark is " + str(NearestLandmark) + " away")
            nearestLandm.place(x=10,y=10)
        
            
            #ball bounces off landmarks
            if  Pos[3] >=540 and Pos[1] <=580 and Pos[2] >= 320 and Pos[0] <= 370:
                YSpeed = -YSpeed
            if  Pos[3] >=160 and Pos[1] <=195 and Pos[2] >= 400 and Pos[0] <= 450:
                XSpeed = -XSpeed
            if  Pos[3] >=40 and Pos[1] <=80 and Pos[2] >= 540 and Pos[0] <= 610:
                YSpeed = -YSpeed
            if  Pos[3] >=360 and Pos[1] <=400 and Pos[2] >= 670 and Pos[0] <= 740:
                XSpeed = -XSpeed
            if  Pos[3] >=400 and Pos[1] <=440 and Pos[2] >= 960 and Pos[0] <= 1000:
                YSpeed = -YSpeed
            if  Pos[3] >=300 and Pos[1] <=340 and Pos[2] >= 1160 and Pos[0] <= 1200:
                XSpeed = -XSpeed

            #Triggering the Power Up square for speed
            if  750 >= PosR[0] <= 800 and 150 <= PosR[0] >= 725 and 175 <= PosR[3] >=150 and 750 >= PosR[1] <=175:
                def leftKey(event):
                    x1,y1,x2,y2 = w.coords(Robot)
                    w.coords(Robot,x1-20,y1,x2-20,y2)

                def rightKey(event):
                    x1,y1,x2,y2= w.coords(Robot)
                    w.coords(Robot,x1+20,y1,x2+20,y2)

                def upKey(event):
                    x1,y1,x2,y2= w.coords(Robot)
                    w.coords(Robot,x1,y1-20,x2,y2-20)

                def downKey(event):
                    x1,y1,x2,y2= w.coords(Robot)
                    w.coords(Robot,x1,y1+20,x2,y2+20)
                w.bind('<Left>', leftKey)
                w.bind('<Right>', rightKey)
                w.bind('<Up>', upKey)
                w.bind('<Down>', downKey)
                
                w.focus_set()
                collectedBoost = Label(root, text = "Speed boost activated!")
                collectedBoost.place(x=10,y=30)
               
                
            rx1, ry1, rx2, ry2 = w.coords(Robot)
            if rx1 >= x_max:
                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)
                cx = -10
            if ry1 <= y_min:
                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS) #Plays a sound when robot hits border
                cy = 10
            if ry2 >= y_max:
                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)
                cy= -10
            if rx1 <= x_min:
                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)
                cx = 10
            w.coords(Robot, rx1+cx, ry1+cy, rx2+cx, ry2+cy)
            cx = 0
            cy = 0

            PosR = w.bbox(Robot)
            #This works out distance between 
            DistanceBetween = int(math.sqrt((int(PosR[2]) - int(Pos[2]))**2 + (int(PosR[3]) - int(Pos[3]))**2))
            
            if DistanceBetween <= 20: #if the value of the distance between the ball and robot is 20 or less, it should lose a life
                print("enemy hit")
                PrintLives()
                time.sleep(0.1)
        
            w.update()
            time.sleep(0.01)
            
    collisionDetection()


def PromptLandMark1():

        StatueLiberty = Label(root, text= "Welcome to the Statue of Liberty\n Location: New York\n Visitors Calculated In 2009: 3.2 Million")
        StatueLiberty.place(x=700, y=400)
        root.after(1500, StatueLiberty.destroy)
        

def PromptLandMark2():

        GoldenGateBridge = Label(root, text= "Welcome to Golden Gate Bridge\n Construction Started: January 1933\n Construction Ended: April 1937")
        GoldenGateBridge.place(x=570, y=80)
        root.after(1500, GoldenGateBridge.destroy)



def PromptLandMark3():

        MountRushmore = Label(root, text= "Welcome to Mount Rushmore\n Height:18metres\n Established: March 1925")
        MountRushmore.place(x=420, y=200)
        root.after(1500, MountRushmore.destroy)


def PromptLandMark4():

        GrandCanyon = Label(root, text= "Welcome to the Grand Canyon\n Age: 5-6 Million Years\n Floor Elevation: 800metres ")
        GrandCanyon.place(x=340, y=580)
        root.after(1500, GrandCanyon.destroy)


def PromptLandMark5():

        WhiteHouse = Label(root, text= "Welcome to The White House\n Constructed In 1792\n Location: Washington DC")
        WhiteHouse.place(x=960, y=440)
        root.after(1500, WhiteHouse.destroy)


def PromptLandMark6():

        EmpireState = Label(root, text= "Welcome to The Empire State Building\n Built in March 1930\n Height: 381m")
        EmpireState.place(x=1000, y=340)
        root.after(1500, EmpireState.destroy)


def RandomPosition(event):
     xcoordinate0 = random.randint(50,680) #randomly selects a number in range 50-680
     ycoordinate0 = xcoordinate0 - 20
     xcoordinate1 = xcoordinate0 + 20
     ycoordinate1 = ycoordinate0 + 20
 
     
     
 
     #moves robot to new coordinates    
     w.coords(Robot,xcoordinate0, ycoordinate0, xcoordinate1, ycoordinate1)
 
w.bind('<r>', RandomPosition) #assigns our function above to the 'r' character on keyboard

distance()

neverEndingFunctions()
    
root.mainloop()
