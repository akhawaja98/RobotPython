while True:

        p = list(w.bbox(Robot)) #get's latest coordinates of robot's position
        

        #checks if robot is near landmark6
        if p[0] >= 1100 and p[0] <= 1230 and p[1] >= 250 and p[1] <= 400 and p[2] >= 1100 and p[2] <= 1300 and p[3] >= 200 and p[3] <= 400:
            PromptLandMark6()
            
        #checks if robot is near landmark5
        elif p[0] >= 900 and p[0] <= 1030 and p[1] >= 350 and p[1] <= 500 and p[2] >= 900 and p[2] <= 1100 and p[3] >= 300 and p[3] <= 500:
            PromptLandMark5()

        #checks if robot is near landmark4
        elif p[0] >= 260 and p[0] <= 410 and p[1] >= 490 and p[1] <= 640 and p[2] >= 280 and p[2] <= 480 and p[3] >= 440 and p[3] <= 640:
            PromptLandMark4()

        
        #checks if robot is near landmark3
        elif p[0] >= 340 and p[0] <= 490 and p[1] >= 110 and p[1] <= 260 and p[2] >= 360 and p[2] <= 560 and p[3] >= 60 and p[3] <= 260:
            PromptLandMark3()

        #checks if robot is near landmark2
        elif p[0] >= 490 and p[0] <= 640 and p[1] >= 0 and p[1] <= 140 and p[2] >= 510 and p[2] <= 710 and p[3] >= 0 and p[3] <= 140:
            PromptLandMark2()

        #checks if robot is near landmark1
        elif p[0] >= 620 and p[0] <= 770 and p[1] >=310  and p[1] <= 460 and p[2] >= 640 and p[2] <= 840 and p[3] >= 220 and p[3] <= 440:
            PromptLandMark1()
        

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
