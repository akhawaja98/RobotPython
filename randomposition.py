import tkinter, random, turtle


root = tk()

canvas = Canvas(root, width = 200, height = 200)

xcoordinate = random.randint(20,300) #creates a random x coordinate
ycoordinate = random.randint(20,300) #creates a random y coordinate


randomcoordinates = (str((xcoordinate, ycoordinate)))
print(randomcoordinates)

turtle.forward(xcoordinate) 
turtle.left(90)
turtle.forward(ycoordinate) #draws the path using the random coordinates above

#currently uses turtle, will move to a tkinter window soon

root.mainloop()
