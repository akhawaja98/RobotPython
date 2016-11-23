def neverEndingFunctions():
    def collisionDetection():
        cx = 0
        cy = 0
        ball = w.create_oval(10,10,60,60, fill="#FF0000")
        XSpeed = 1
        YSpeed = 2


    
        while True:
            w.move(ball, XSpeed, YSpeed)
            Pos = w.coords(ball)
            if Pos[3] >=720 or Pos[1] <=0:
                YSpeed = -YSpeed
            if Pos[2] >=1280 or Pos[0] <=0:
                XSpeed = -XSpeed

            w.move(ball, XSpeed, YSpeed)
            if 700 >= Pos[3] or 740 <= Pos[1]: #bounces off landmark 1
                XSpeed = -XSpeed
            if 360 >= Pos[2] or 400 <= Pos[0]:
                YSpeed = -YSpeed
                
            w.move(ball, XSpeed, YSpeed)
            if 570 >= Pos[3] or 610 <= Pos[1]: #bounces off landmark 2
                XSpeed = -XSpeed
            if 80 >= Pos[2] or 40 <= Pos[0]:
                YSpeed = -YSpeed

            w.move(ball, XSpeed, YSpeed)
            if 420 >= Pos[3] or 460 <= Pos[1]: #bounces off landmark 3
                XSpeed = -XSpeed
            if 200 >= Pos[2] or 160 <= Pos[0]:
                YSpeed = -YSpeed

            w.move(ball, XSpeed, YSpeed)
            if 340 >= Pos[3] or 380 <= Pos[1]: #bounces off landmark 4
                XSpeed = -XSpeed
            if 580 >= Pos[2] or 540 <= Pos[0]:
                YSpeed = -YSpeed

            w.move(ball, XSpeed, YSpeed)
            if 960 >= Pos[3] or 1000 <= Pos[1]: #bounces off landmark 5
                XSpeed = -XSpeed
            if 440 >= Pos[2] or 400 <= Pos[0]:
                YSpeed = -YSpeed

            w.move(ball, XSpeed, YSpeed)
            if 1160 >= Pos[3] or 1200 <= Pos[1]: #bounces off landmark 6
                XSpeed = -XSpeed
            if 340 >= Pos[2] or 300 <= Pos[0]:
                YSpeed = -YSpeed
                
            rx1, ry1, rx2, ry2 = w.coords(Robot)
            if rx1 >= x_max:
                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)
                cx = -10
            if ry1 <= y_min:
                winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS)
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
        
            w.update()
            time.sleep(0.01)
            
    collisionDetection()

distance()

neverEndingFunctions()
    
root.mainloop()
