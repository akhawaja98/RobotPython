def RandomPosition(event):
    xcoordinate0 = random.randint(50,680) #randomly selects a number in range 50-680
    ycoordinate0 = xcoordinate0 - 20
    xcoordinate1 = xcoordinate0 + 20
    ycoordinate1 = ycoordinate0 + 20

    
    

    #moves robot to new coordinates    
    w.coords(Robot,xcoordinate0, ycoordinate0, xcoordinate1, ycoordinate1)



w.bind('<r>', RandomPosition) #assigns our function above to the 'r' character on keyboard
w.focus_set()
