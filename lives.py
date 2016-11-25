global startlives
startlives = 4


def PrintLives():    
    global startlives 
    startliveslabel = Label(root, text= "You Have 3 Lives, Good Luck", font="Times")
    startliveslabel.place(x=100, y=30) #positioning the lives label in a suitable area of the canvas

    
    startlives -= 1
    startliveslabel.config(text="You Have " + str(startlives) + " Lives") #.config allows us to change the labels text

    if startlives <= 0:
        startliveslabel.config(text="GAME OVER - No Lives Left")
        
        root.destroy()


    if startlives == 1:
        startliveslabel.config(text="You Have 1 Life Left")

loselifebtn = Button(root, text="Lost Life", command=PrintLives)  #executes the PrintLives function above
loselifebtn.pack()
