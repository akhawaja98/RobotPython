#FOR LANDMARK 1 
#Detect left side of object
            if 740>(Pos[3] - 10) and 740<(Pos[1]+10) and 400< Pos[2] and 400>Pos[0]:
                XSpeed = -XSpeed
#Detect right side of object
            if 700<(Pos[1] + 10) and 700>(Pos[3] - 10) and 400< Pos[2] and 400>Pos[0]:
                XSpeed = -XSpeed
#Detect bottom of object
            if 400>(Pos[2] - 10) and 400<(Pos[2]+10) and 700>Pos[3] and 700<Pos[1]:
                YSpeed = -YSpeed
#Detect top of object
            if 400>(Pos[0] - 10) and 400<(Pos[0]+10) and 700>Pos[3] and 700<Pos[1]:
                YSpeed = -YSpeed


            
