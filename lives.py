global startlives
startlives = 101


def PrintLives():    
    global startlives 
    startliveslabel = Label(root, text= "Health 100%", font="Times")
    startliveslabel.place(x=100, y=30) #positioning the lives label in a suitable area of the canvas

    
    startlives -= 1
    startliveslabel.config(text="Health = " + str(startlives) + "%") #.config allows us to change the labels text

    if startlives <= 0:
        root.destroy()


    if startlives == 1:
        startliveslabel.config(text="1% Health Left Be Careful")

loselifebtn = Button(root, text="Lost Life", command=PrintLives)  #executes the PrintLives function above
loselifebtn.pack()
