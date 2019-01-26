import turtle
turtle.screensize()


turtle.pensize()
turtle.pencolor("black")
turtle.setheading(90)
primespeed= 1
for k in range(2):                
    for j in range(60):
        if j < 30:
            primespeed += 0.2     
        else:
            primespeed -= 0.2     
        turtle.forward(primespeed)
        turtle.left(3)            

