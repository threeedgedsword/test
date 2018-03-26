import turtle

# Initialize the turtle and the screen 
ima = turtle.Screen()
mela = turtle.Turtle()
mela.pensize(5)
mela.shape("turtle")

'''# Outer rectangle set-up
mela.speed(0)   # speeds up sketching, zero means no animation, ie, automatic
mela.up()
mela.color("blue")
mela.pensize(3)
mela.goto(-110,-160)
mela.down()
for index in range(2):
    mela.forward(220)
    mela.left(90)
    mela.forward(320)
    mela.left(90)

# Inner rectangle set-up
mela.up()
mela.color("red")
mela.goto(-100,-150)
mela.down()
for index in range(2):
    mela.forward(200)
    mela.left(90)
    mela.forward(300)
    mela.left(90)

# Grid set-up
mela.up()
mela.color("green")

# Vertical bar
mela.goto(0,150)
mela.down()
mela.right(90)
mela.forward(300)
mela.left(90)

# Top horizontal bar
mela.up()
mela.goto(-100, 50)
mela.down()
mela.forward(200)

# Bottom horizontal bar
mela.up()
mela.goto(-100, -50)
mela.down()
mela.forward(200) 

mela.color("black") # Change the color of the Mela turtle and move Mela'''

# turtle without leaving a trail
mela.up()
mela.goto(-110,-160)

# Draw an M
mela.goto(-100, -150)
mela.down()
mela.goto(-100, 150)
mela.goto(0,0)
mela.goto(100, 150)
mela.goto(100,-150)
mela.up()
mela.goto(110,-160)

# Ensure that you can close the window that you created. 
ima.exitonclick()
