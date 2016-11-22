def neverEndingFunctions():
    def collisionDetection():
        cx = 0
        cy = 0
        ball = w.create_oval(10,10,60,60, fill="#FF0000")
        XSpeed = 1
        YSpeed = 2

        landm1 = w.coords(Landmark)
        landm2 = w.coords(Landmark2)
        landm3 = w.coords(Landmark3)
        landm4 = w.coords(Landmark4)
        landm5 = w.coords(Landmark5)
        landm6 = w.coords(Landmark6)
    
        while True:
            w.move(ball, XSpeed, YSpeed)
            Pos = w.coords(ball)
            if Pos[3] >=720 or Pos[1] <=0:
                YSpeed = -YSpeed
            if Pos[2] >=1280 or Pos[0] <=0:
                XSpeed = -XSpeed

            w.move(ball, XSpeed, YSpeed)
            landm1 = w.coords(Landmark)
            if landm1 == Pos[3] or landm1 == Pos[1]: 
                XSpeed = -XSpeed
            if landm1 == Pos[2] or landm1 == Pos[0]:
                YSpeed = -YSpeed
                
            w.move(ball, XSpeed, YSpeed)
            landm2 = w.coords(Landmark2)
            if landm2 == Pos[3] or landm2 == Pos[1]: 
                XSpeed = -XSpeed
            if landm2 == Pos[2] or landm2 == Pos[0]:
                YSpeed = -YSpeed

            w.move(ball, XSpeed, YSpeed)
            landm3 = w.coords(Landmark3)
            if landm3 == Pos[3] or landm3 == Pos[1]: 
                XSpeed = -XSpeed
            if landm3 == Pos[2] or landm3 == Pos[0]:
                YSpeed = -YSpeed

            landm4 = w.coords(Landmark4)
            if landm4 == Pos[3] or landm4 == Pos[1]: 
                XSpeed = -XSpeed
            if landm4 == Pos[2] or landm4 == Pos[0]:
                YSpeed = -YSpeed

            landm5 = w.coords(Landmark5)
            if landm5 == Pos[3] or landm5 == Pos[1]: 
                XSpeed = -XSpeed
            if landm5 == Pos[2] or landm5 == Pos[0]:
                YSpeed = -YSpeed

            landm6 = w.coords(Landmark6)
            if landm6 == Pos[3] or landm6 == Pos[1]: 
                XSpeed = -XSpeed
            if landm6 == Pos[2] or landm6 == Pos[0]:
                YSpeed = -YSpeed
